import mysql.connector
from tabulate import tabulate
import face_recognition
import cv2
import numpy as np
import os

con= mysql.connector.connect(host='bj5csujb9fw4no3sjaci-mysql.services.clever-cloud.com',user='u9inrn5qotml9y1s',password='dQyinNkc2ZA32HjtXIGw',database='bj5csujb9fw4no3sjaci')
#con=mysql.connector.connect(host="localhost", user="root", password="", database="student")
fd=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
Ś
if con:
    print("\n==DataBase Connected==\n")
else:
    print("==DataBase not Connected==")


def capture_image(name):
    cam = cv2.VideoCapture(0)

    print("Press 's' to take a picture")

    while True:
        ret, frame = cam.read()  # Capture frame-by-frame
        # Check if the frame was successfully read
        if not ret:
            print("Error: Failed to capture frame from camera.")
            # Instead of just breaking, return None to signal failure
            return None
        cv2_imshow(frame)  # Display the resulting frame

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            frame=cv2.flip(frame,1)
            print("Image captured and saved as:")
            cv2_imshow(frame)
            cv2.waitKey(0)  # Display the image until any key is pressed
            break

        elif key == ord('q'):
            # Exit the loop if 'q' is pressed
            print("Exiting without capturing an image.")
            # Return None to signal that no image was captured
            return None
    # Release the webcam and close all OpenCV windows
    cam.release()
    cv2.destroyAllWindows()
    _, buffer = cv2.imencode('.jpg', frame)
    image_data = buffer.tobytes()
    #os.remove(f'{name}.jpg')  # Remove the temporary file
    return image_data

def insert():
    reg = input("Reg_No: ")
    name = input("Name: ")
    dept = input("Department: ")
    contact = input("Contact: ")
    contact = input("Contact: ")
    mail = input("Mail_ID: ")
    img=capture_image(name)
    cursor = con.cursor()
    sql = "INSERT INTO student_detail (PROFILE, REG_NO, NAME, DEPARTMENT, CONTACT_NO, MAIL_ID) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (img, reg, name, dept, contact, mail))

    os.remove(f'{name}.jpg')  # Remove the temporary file
    # Inserting into subject tables
    for i in range(1, 5):
        sub_table = f"sub{i}"
        cursor.execure(f"select NO_OF_CLASS from %s", sub_table)
        re=cursor.fetchone()
        cursor.execute("update {sub_table} set NO_OF_CLASS=%s", re)
        sql = f"INSERT INTO {sub_table} (REG_NO) VALUES (%s)"
        cursor.execute(sql, (reg,))

    con.commit()
    print("\n== Detail Added to the Table ==\n")

def update_detail():
    reg=input("Reg_no:")
    print("\n1.Name || 2.Department || 3.Contact || 4.Mail || 5.Profile\n")
    ch=int(input("What you want to Update:"))
    res=con.cursor()
    if ch==1:
        name=input("Enter Name:")
        sql="update student_detail set NAME=%s where REG_NO=%s"
        res.execute(sql,(name, reg))
        con.commit()
        print("\n==Student Detail updated Successfully==\n")
    elif ch==2:
        name=input("Enter Department:")
        sql="update student_detail set DEPARTMENT=%s where REG_NO=%s"
        res.execute(sql,(name, reg))
        con.commit()
        print("\n==Student Detail updated Successfully==\n")
    elif ch==3:
        name=input("Enter Contact:")
        sql="update student_detail set CONTACT_NO=%s where REG_NO=%s"
        res.execute(sql,(name, reg))
        con.commit()
        print("\n==Student Detail updated Successfully==\n")
    elif ch==4:
        name=input("Enter Mail_ID:")
        sql="update student_detail set MAIL_ID=%s where REG_NO=%s"
        res.execute(sql,(name, reg))
        con.commit()
        print("\n==Student Detail updated Successfully==\n")
    elif ch==5:
        img=capture_image(reg)
        res.execute(f"update student_detail set PROFILE=%s where REG_NO=%s",(img,reg))
        con.commit()
        print('\n==Profile Updated==\n')

def update_mark(sub):
    reg = input("Reg_No: ")
    ia1 = float(input("IAE_1: "))
    ia2 = float(input("IAE_2: "))
    ia3 = float(input("IAE_3: "))

    cursor = con.cursor()
    sql = f"UPDATE {sub} SET IAE_1=%s, IAE_2=%s, IAE_3=%s WHERE REG_NO = %s"
    cursor.execute(sql, (ia1, ia2, ia3, reg))

    con.commit()
    print("\n==Mark Added Successfully==\n")

def delete():
    ch=input("Which Reg_No you want to Delete:")
    re=con.cursor()
    sql="delete from student_detail where REG_NO=%s"
    re.execute(sql,(ch,))
    for i in range(1,5):
        sub=f"sub{i}"
        sql=f"delete from {sub} where REG_NO=%s"
        re.execute(sql,(ch,))
    con.commit()
    print("\n==Student Detail Deleted Successfully==\n")

def view(sub):
    cursor = con.cursor()
    sql = f"SELECT student_detail.REG_NO, NAME, DEPARTMENT, CONTACT_NO, MAIL_ID, IAE_1, IAE_2, IAE_3, NO_OF_CLASS, NO_OF_PRESENT, ATTENDANCE FROM student_detail, {sub} WHERE student_detail.REG_NO = {sub}.REG_NO ORDER BY student_detail.REG_NO"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(result,headers=['REG_NO', 'NAME', 'DEPARTMENT', 'CONTACT_NO', 'MAIL_ID', 'IAE_1', 'IAE_2', 'IAE_3', 'NO_OF_CLASS', 'NO_OF_PRESENT', 'ATTENDANCE']))

    cursor.execute("SELECT PROFILE, NAME FROM student_detail")
    profiles = cursor.fetchall()
    for profile, name in profiles:
        image_array = np.frombuffer(profile, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        cv2_imshow(image)
        cv2.waitKey(0) # Display each image for 1 second cv2.destroyAllWindows()
    cv2.destroyAllWindows()

def update_attendance(reg_no, sub):
    cursor = con.cursor()
    sql = f"SELECT NO_OF_CLASS, NO_OF_PRESENT FROM {sub} WHERE REG_NO = %s"
    cursor.execute(sql, (reg_no,))
    result = cursor.fetchone()
    if result:
        no_of_class, no_of_present = result
        attendance = (no_of_present / no_of_class) * 100
        sql = f"UPDATE {sub} SET NO_OF_PRESENT = NO_OF_PRESENT + 1, ATTENDANCE = %s WHERE REG_NO = %s"
        cursor.execute(sql, (attendance, reg_no))
        con.commit()
        print(f"Attendance updated for {reg_no} in {sub}")
    else:
        print("Unknown face detected")

def fetch_known_faces():
    cursor = con.cursor()
    cursor.execute("SELECT PROFILE, REG_NO FROM student_detail")
    profiles = cursor.fetchall()
    known_faces = []
    known_reg_nos = []
    for profile, reg_no in profiles:
        image_array = np.frombuffer(profile, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_locations = face_recognition.face_locations(gray_image)
        face_encodings = face_recognition.face_encodings(gray_image, face_locations)
        if face_encodings:
            known_faces.append(face_encodings[0])
            known_reg_nos.append(reg_no)
    return known_faces, known_reg_nos

def recognize_and_update(sub):
    print('\n======recognize_and_update called')
    cursor = con.cursor()
    cursor.execute(f"UPDATE {sub} SET NO_OF_CLASS = NO_OF_CLASS + 1")
    con.commit()
    # Fetch known faces from the database
    known_faces, known_reg_nos = fetch_known_faces()
    print('\n=========fetch_known_faces returned')
    # Capture the group photo
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if ret:
            cv2_imshow(frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cam.release()
                cv2.imwrite('group_photo.jpg', frame)
                print("Group photo captured successfully.")
                break
        else:
            print("Failed to capture group photo.")
            cam.release()
            break
    cv2.destroyAllWindows()

    # Load the captured group photo
    image = face_recognition.load_image_file('group_photo.jpg')
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        face_distances = face_recognition.face_distance(known_faces, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            reg_no = known_reg_nos[best_match_index]
            print(f"Face recognized: {reg_no}")
            update_attendance(reg_no, sub)
    print(f"Attendance updated for subject {sub}")

def teacher():
    print("\n\tSUB_1 || SUB_2 || SUB_3 || SUB_4\n")
    wht = int(input("Select subject: "))
    if wht == 1:
        sub = "sub1"
    elif wht == 2:
        sub = "sub2"
    elif wht == 3:
        sub = "sub3"
    elif wht == 4:
        sub = "sub4"
    else:
        print("\n== Invalid input ==\n")
        return
    print("\n")
    ch = int(input("(1.Attendance || 2.Detail) : "))
    if ch == 2:
        while True:
            print('\n\t1.Insert || 2.Update || 3.Delete || 4.View || 5.Quit\n')
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                insert()

            elif choice == 2:
                wht = int(input("\n(1.Detail || 2.Mark) : "))
                if wht == 1:
                    update_detail()
                elif wht == 2:
                    update_mark(sub)

            elif choice == 3:
                delete()

            elif choice == 4:
                view(sub)

            elif choice == 5:
                exit()

            else:
                print("\n== Enter Valid Input ==\n")
    elif ch == 1:
        recognize_and_update(sub)

def student():
    reg=input("Reg_No:")
    res=con.cursor()

    sql=f"select REG_NO, NAME, DEPARTMENT, CONTACT_NO, MAIL_ID from student_detail where REG_NO={reg}"
    res.execute(sql)
    re=res.fetchall()
    print("\n======STUDENT DETAIL======\n")
    print(tabulate(re, headers=["REG_NO",'NAME','DEPARTMENT','CONTACT','MAIL_ID']))
    for i in range(1,5):
        sub=f"sub{i}"
        sql=f"select IAE_1, IAE_2, IAE_3, NO_OF_CLASS, NO_OF_PRESENT, ATTENDANCE from {sub} where REG_NO={reg}"
        res.execute(sql)
        re=res.fetchall()
        print(f"\n======SUBJECT {i}======\n")
        print(tabulate(re, headers=['IAE_1','IAE_2','IAE_3','NO_OF_CLASS','NO_OF_PRESENT','ATTENDANCE_PERC']))

    res.execute("SELECT PROFILE FROM student_detail WHERE REG_NO = %s", (reg,))
    result = res.fetchone()
    if result:
        result=result[0]
        image_array=np.frombuffer(result, dtype=np.uint8)
        image=cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        cv2_imshow(image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("==No Photo found !==")

if __name__=='__main__':
    print("1.Staff || 2.Student")
    who=int(input("Who are you:"))
    if who==1:
        teacher()
    elif who==2:
        student()
    else:
        print("==Invalied Input!==")
