{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "epZFWyvTGCxP"
      },
      "outputs": [],
      "source": [
        "import mysql.connector\n",
        "from tabulate import tabulate\n",
        "import face_recognition\n",
        "import cv2\n",
        "import numpy as np\n",
        "import os"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "con= mysql.connector.connect(host='bj5csujb9fw4no3sjaci-mysql.services.clever-cloud.com',user='u9inrn5qotml9y1s',password='dQyinNkc2ZA32HjtXIGw',database='bj5csujb9fw4no3sjaci')\n",
        "#con=mysql.connector.connect(host=\"localhost\", user=\"root\", password=\"\", database=\"student\")\n",
        "fd=cv2.CascadeClassifier(\"haarcascade_frontalface_default.xml\")\n",
        "Ś\n",
        "if con:\n",
        "    print(\"\\n==DataBase Connected==\\n\")\n",
        "else:\n",
        "    print(\"==DataBase not Connected==\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PVz_y7bx-0C6",
        "outputId": "534a9bee-bea5-4f5a-9e62-dcd58b45c6f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "==DataBase Connected==\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def capture_image(name):\n",
        "    cam = cv2.VideoCapture(0)\n",
        "\n",
        "    print(\"Press 's' to take a picture\")\n",
        "\n",
        "    while True:\n",
        "        ret, frame = cam.read()  # Capture frame-by-frame\n",
        "        # Check if the frame was successfully read\n",
        "        if not ret:\n",
        "            print(\"Error: Failed to capture frame from camera.\")\n",
        "            # Instead of just breaking, return None to signal failure\n",
        "            return None\n",
        "        cv2_imshow(frame)  # Display the resulting frame\n",
        "\n",
        "        key = cv2.waitKey(1) & 0xFF\n",
        "\n",
        "        if key == ord('s'):\n",
        "            frame=cv2.flip(frame,1)\n",
        "            print(\"Image captured and saved as:\")\n",
        "            cv2_imshow(frame)\n",
        "            cv2.waitKey(0)  # Display the image until any key is pressed\n",
        "            break\n",
        "\n",
        "        elif key == ord('q'):\n",
        "            # Exit the loop if 'q' is pressed\n",
        "            print(\"Exiting without capturing an image.\")\n",
        "            # Return None to signal that no image was captured\n",
        "            return None\n",
        "    # Release the webcam and close all OpenCV windows\n",
        "    cam.release()\n",
        "    cv2.destroyAllWindows()\n",
        "    _, buffer = cv2.imencode('.jpg', frame)\n",
        "    image_data = buffer.tobytes()\n",
        "    #os.remove(f'{name}.jpg')  # Remove the temporary file\n",
        "    return image_data"
      ],
      "metadata": {
        "id": "z_kxTykk-6ZT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def insert():\n",
        "    reg = input(\"Reg_No: \")\n",
        "    name = input(\"Name: \")\n",
        "    dept = input(\"Department: \")\n",
        "    contact = input(\"Contact: \")\n",
        "    contact = input(\"Contact: \")\n",
        "    mail = input(\"Mail_ID: \")\n",
        "    img=capture_image(name)\n",
        "    cursor = con.cursor()\n",
        "    sql = \"INSERT INTO student_detail (PROFILE, REG_NO, NAME, DEPARTMENT, CONTACT_NO, MAIL_ID) VALUES (%s, %s, %s, %s, %s, %s)\"\n",
        "    cursor.execute(sql, (img, reg, name, dept, contact, mail))\n",
        "\n",
        "    os.remove(f'{name}.jpg')  # Remove the temporary file\n",
        "    # Inserting into subject tables\n",
        "    for i in range(1, 5):\n",
        "        sub_table = f\"sub{i}\"\n",
        "        cursor.execure(f\"select NO_OF_CLASS from %s\", sub_table)\n",
        "        re=cursor.fetchone()\n",
        "        cursor.execute(\"update {sub_table} set NO_OF_CLASS=%s\", re)\n",
        "        sql = f\"INSERT INTO {sub_table} (REG_NO) VALUES (%s)\"\n",
        "        cursor.execute(sql, (reg,))\n",
        "\n",
        "    con.commit()\n",
        "    print(\"\\n== Detail Added to the Table ==\\n\")"
      ],
      "metadata": {
        "id": "PEge84Ll-__z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def update_detail():\n",
        "    reg=input(\"Reg_no:\")\n",
        "    print(\"\\n1.Name || 2.Department || 3.Contact || 4.Mail || 5.Profile\\n\")\n",
        "    ch=int(input(\"What you want to Update:\"))\n",
        "    res=con.cursor()\n",
        "    if ch==1:\n",
        "        name=input(\"Enter Name:\")\n",
        "        sql=\"update student_detail set NAME=%s where REG_NO=%s\"\n",
        "        res.execute(sql,(name, reg))\n",
        "        con.commit()\n",
        "        print(\"\\n==Student Detail updated Successfully==\\n\")\n",
        "    elif ch==2:\n",
        "        name=input(\"Enter Department:\")\n",
        "        sql=\"update student_detail set DEPARTMENT=%s where REG_NO=%s\"\n",
        "        res.execute(sql,(name, reg))\n",
        "        con.commit()\n",
        "        print(\"\\n==Student Detail updated Successfully==\\n\")\n",
        "    elif ch==3:\n",
        "        name=input(\"Enter Contact:\")\n",
        "        sql=\"update student_detail set CONTACT_NO=%s where REG_NO=%s\"\n",
        "        res.execute(sql,(name, reg))\n",
        "        con.commit()\n",
        "        print(\"\\n==Student Detail updated Successfully==\\n\")\n",
        "    elif ch==4:\n",
        "        name=input(\"Enter Mail_ID:\")\n",
        "        sql=\"update student_detail set MAIL_ID=%s where REG_NO=%s\"\n",
        "        res.execute(sql,(name, reg))\n",
        "        con.commit()\n",
        "        print(\"\\n==Student Detail updated Successfully==\\n\")\n",
        "    elif ch==5:\n",
        "        img=capture_image(reg)\n",
        "        res.execute(f\"update student_detail set PROFILE=%s where REG_NO=%s\",(img,reg))\n",
        "        con.commit()\n",
        "        print('\\n==Profile Updated==\\n')"
      ],
      "metadata": {
        "id": "Iz8Exe8h_DHs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def update_mark(sub):\n",
        "    reg = input(\"Reg_No: \")\n",
        "    ia1 = float(input(\"IAE_1: \"))\n",
        "    ia2 = float(input(\"IAE_2: \"))\n",
        "    ia3 = float(input(\"IAE_3: \"))\n",
        "\n",
        "    cursor = con.cursor()\n",
        "    sql = f\"UPDATE {sub} SET IAE_1=%s, IAE_2=%s, IAE_3=%s WHERE REG_NO = %s\"\n",
        "    cursor.execute(sql, (ia1, ia2, ia3, reg))\n",
        "\n",
        "    con.commit()\n",
        "    print(\"\\n==Mark Added Successfully==\\n\")"
      ],
      "metadata": {
        "id": "EKjsE4xQ_F_v"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def delete():\n",
        "    ch=input(\"Which Reg_No you want to Delete:\")\n",
        "    re=con.cursor()\n",
        "    sql=\"delete from student_detail where REG_NO=%s\"\n",
        "    re.execute(sql,(ch,))\n",
        "    for i in range(1,5):\n",
        "        sub=f\"sub{i}\"\n",
        "        sql=f\"delete from {sub} where REG_NO=%s\"\n",
        "        re.execute(sql,(ch,))\n",
        "    con.commit()\n",
        "    print(\"\\n==Student Detail Deleted Successfully==\\n\")"
      ],
      "metadata": {
        "id": "jReBiy5o_JAI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def view(sub):\n",
        "    cursor = con.cursor()\n",
        "    sql = f\"SELECT student_detail.REG_NO, NAME, DEPARTMENT, CONTACT_NO, MAIL_ID, IAE_1, IAE_2, IAE_3, NO_OF_CLASS, NO_OF_PRESENT, ATTENDANCE FROM student_detail, {sub} WHERE student_detail.REG_NO = {sub}.REG_NO ORDER BY student_detail.REG_NO\"\n",
        "    cursor.execute(sql)\n",
        "    result = cursor.fetchall()\n",
        "    print(tabulate(result,headers=['REG_NO', 'NAME', 'DEPARTMENT', 'CONTACT_NO', 'MAIL_ID', 'IAE_1', 'IAE_2', 'IAE_3', 'NO_OF_CLASS', 'NO_OF_PRESENT', 'ATTENDANCE']))\n",
        "\n",
        "    cursor.execute(\"SELECT PROFILE, NAME FROM student_detail\")\n",
        "    profiles = cursor.fetchall()\n",
        "    for profile, name in profiles:\n",
        "        image_array = np.frombuffer(profile, dtype=np.uint8)\n",
        "        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)\n",
        "        cv2_imshow(image)\n",
        "        cv2.waitKey(0) # Display each image for 1 second cv2.destroyAllWindows()\n",
        "    cv2.destroyAllWindows()"
      ],
      "metadata": {
        "id": "1Qp5chAp_PES"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def update_attendance(reg_no, sub):\n",
        "    cursor = con.cursor()\n",
        "    sql = f\"SELECT NO_OF_CLASS, NO_OF_PRESENT FROM {sub} WHERE REG_NO = %s\"\n",
        "    cursor.execute(sql, (reg_no,))\n",
        "    result = cursor.fetchone()\n",
        "    if result:\n",
        "        no_of_class, no_of_present = result\n",
        "        attendance = (no_of_present / no_of_class) * 100\n",
        "        sql = f\"UPDATE {sub} SET NO_OF_PRESENT = NO_OF_PRESENT + 1, ATTENDANCE = %s WHERE REG_NO = %s\"\n",
        "        cursor.execute(sql, (attendance, reg_no))\n",
        "        con.commit()\n",
        "        print(f\"Attendance updated for {reg_no} in {sub}\")\n",
        "    else:\n",
        "        print(\"Unknown face detected\")"
      ],
      "metadata": {
        "id": "dAG5WMAv_Ryr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def fetch_known_faces():\n",
        "    cursor = con.cursor()\n",
        "    cursor.execute(\"SELECT PROFILE, REG_NO FROM student_detail\")\n",
        "    profiles = cursor.fetchall()\n",
        "    known_faces = []\n",
        "    known_reg_nos = []\n",
        "    for profile, reg_no in profiles:\n",
        "        image_array = np.frombuffer(profile, dtype=np.uint8)\n",
        "        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)\n",
        "        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
        "        face_locations = face_recognition.face_locations(gray_image)\n",
        "        face_encodings = face_recognition.face_encodings(gray_image, face_locations)\n",
        "        if face_encodings:\n",
        "            known_faces.append(face_encodings[0])\n",
        "            known_reg_nos.append(reg_no)\n",
        "    return known_faces, known_reg_nos"
      ],
      "metadata": {
        "id": "C17H9l6G_Tlw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def recognize_and_update(sub):\n",
        "    print('\\n======recognize_and_update called')\n",
        "    cursor = con.cursor()\n",
        "    cursor.execute(f\"UPDATE {sub} SET NO_OF_CLASS = NO_OF_CLASS + 1\")\n",
        "    con.commit()\n",
        "    # Fetch known faces from the database\n",
        "    known_faces, known_reg_nos = fetch_known_faces()\n",
        "    print('\\n=========fetch_known_faces returned')\n",
        "    # Capture the group photo\n",
        "    cam = cv2.VideoCapture(0)\n",
        "    while True:\n",
        "        ret, frame = cam.read()\n",
        "        if ret:\n",
        "            cv2_imshow(frame)\n",
        "            if cv2.waitKey(1) & 0xFF == ord('s'):\n",
        "                cam.release()\n",
        "                cv2.imwrite('group_photo.jpg', frame)\n",
        "                print(\"Group photo captured successfully.\")\n",
        "                break\n",
        "        else:\n",
        "            print(\"Failed to capture group photo.\")\n",
        "            cam.release()\n",
        "            break\n",
        "    cv2.destroyAllWindows()\n",
        "\n",
        "    # Load the captured group photo\n",
        "    image = face_recognition.load_image_file('group_photo.jpg')\n",
        "    face_locations = face_recognition.face_locations(image)\n",
        "    face_encodings = face_recognition.face_encodings(image, face_locations)\n",
        "\n",
        "    for face_encoding in face_encodings:\n",
        "        matches = face_recognition.compare_faces(known_faces, face_encoding)\n",
        "        face_distances = face_recognition.face_distance(known_faces, face_encoding)\n",
        "        best_match_index = np.argmin(face_distances)\n",
        "        if matches[best_match_index]:\n",
        "            reg_no = known_reg_nos[best_match_index]\n",
        "            print(f\"Face recognized: {reg_no}\")\n",
        "            update_attendance(reg_no, sub)\n",
        "    print(f\"Attendance updated for subject {sub}\")"
      ],
      "metadata": {
        "id": "l67PZ35Z_X7j"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def teacher():\n",
        "    print(\"\\n\\tSUB_1 || SUB_2 || SUB_3 || SUB_4\\n\")\n",
        "    wht = int(input(\"Select subject: \"))\n",
        "    if wht == 1:\n",
        "        sub = \"sub1\"\n",
        "    elif wht == 2:\n",
        "        sub = \"sub2\"\n",
        "    elif wht == 3:\n",
        "        sub = \"sub3\"\n",
        "    elif wht == 4:\n",
        "        sub = \"sub4\"\n",
        "    else:\n",
        "        print(\"\\n== Invalid input ==\\n\")\n",
        "        return\n",
        "    print(\"\\n\")\n",
        "    ch = int(input(\"(1.Attendance || 2.Detail) : \"))\n",
        "    if ch == 2:\n",
        "        while True:\n",
        "            print('\\n\\t1.Insert || 2.Update || 3.Delete || 4.View || 5.Quit\\n')\n",
        "            choice = int(input(\"Enter Your Choice: \"))\n",
        "            if choice == 1:\n",
        "                insert()\n",
        "\n",
        "            elif choice == 2:\n",
        "                wht = int(input(\"\\n(1.Detail || 2.Mark) : \"))\n",
        "                if wht == 1:\n",
        "                    update_detail()\n",
        "                elif wht == 2:\n",
        "                    update_mark(sub)\n",
        "\n",
        "            elif choice == 3:\n",
        "                delete()\n",
        "\n",
        "            elif choice == 4:\n",
        "                view(sub)\n",
        "\n",
        "            elif choice == 5:\n",
        "                exit()\n",
        "\n",
        "            else:\n",
        "                print(\"\\n== Enter Valid Input ==\\n\")\n",
        "    elif ch == 1:\n",
        "        recognize_and_update(sub)"
      ],
      "metadata": {
        "id": "Mmu6QJo2_cFm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def student():\n",
        "    reg=input(\"Reg_No:\")\n",
        "    res=con.cursor()\n",
        "\n",
        "    sql=f\"select REG_NO, NAME, DEPARTMENT, CONTACT_NO, MAIL_ID from student_detail where REG_NO={reg}\"\n",
        "    res.execute(sql)\n",
        "    re=res.fetchall()\n",
        "    print(\"\\n======STUDENT DETAIL======\\n\")\n",
        "    print(tabulate(re, headers=[\"REG_NO\",'NAME','DEPARTMENT','CONTACT','MAIL_ID']))\n",
        "    for i in range(1,5):\n",
        "        sub=f\"sub{i}\"\n",
        "        sql=f\"select IAE_1, IAE_2, IAE_3, NO_OF_CLASS, NO_OF_PRESENT, ATTENDANCE from {sub} where REG_NO={reg}\"\n",
        "        res.execute(sql)\n",
        "        re=res.fetchall()\n",
        "        print(f\"\\n======SUBJECT {i}======\\n\")\n",
        "        print(tabulate(re, headers=['IAE_1','IAE_2','IAE_3','NO_OF_CLASS','NO_OF_PRESENT','ATTENDANCE_PERC']))\n",
        "\n",
        "    res.execute(\"SELECT PROFILE FROM student_detail WHERE REG_NO = %s\", (reg,))\n",
        "    result = res.fetchone()\n",
        "    if result:\n",
        "        result=result[0]\n",
        "        image_array=np.frombuffer(result, dtype=np.uint8)\n",
        "        image=cv2.imdecode(image_array, cv2.IMREAD_COLOR)\n",
        "        cv2_imshow(image)\n",
        "        cv2.waitKey(0)\n",
        "        cv2.destroyAllWindows()\n",
        "    else:\n",
        "        print(\"==No Photo found !==\")"
      ],
      "metadata": {
        "id": "ulv0DGSq_f5h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__=='__main__':\n",
        "    print(\"1.Staff || 2.Student\")\n",
        "    who=int(input(\"Who are you:\"))\n",
        "    if who==1:\n",
        "        teacher()\n",
        "    elif who==2:\n",
        "        student()\n",
        "    else:\n",
        "        print(\"==Invalied Input!==\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 755
        },
        "id": "N6AW6QDO9DFk",
        "outputId": "cfd39315-658e-4488-f2bb-5b9729695664"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.Staff || 2.Student\n",
            "Who are you:1\n",
            "\n",
            "\tSUB_1 || SUB_2 || SUB_3 || SUB_4\n",
            "\n",
            "Select subject: 1\n",
            "\n",
            "\n",
            "(1.Attendance || 2.Detail) : 2\n",
            "\n",
            "\t1.Insert || 2.Update || 3.Delete || 4.View || 5.Quit\n",
            "\n",
            "Enter Your Choice: 1\n",
            "Reg_No: 08\n",
            "Name: padma\n",
            "Department: aiml\n",
            "Contact: 63895\n",
            "Mail_ID: asd@\n",
            "Press 's' to take a picture\n",
            "Error: Failed to capture frame from camera.\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "IntegrityError",
          "evalue": "1048 (23000): Column 'PROFILE' cannot be null",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mMySQLInterfaceError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/mysql/connector/connection_cext.py\u001b[0m in \u001b[0;36mcmd_query\u001b[0;34m(self, query, raw, buffered, raw_as_string)\u001b[0m\n\u001b[1;32m    705\u001b[0m                 \u001b[0mquery\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mquery\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mencode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"utf-8\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 706\u001b[0;31m             self._cmysql.query(\n\u001b[0m\u001b[1;32m    707\u001b[0m                 \u001b[0mquery\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mMySQLInterfaceError\u001b[0m: Column 'PROFILE' cannot be null",
            "\nThe above exception was the direct cause of the following exception:\n",
            "\u001b[0;31mIntegrityError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-81-94795f4cf264>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mwho\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Who are you:\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mwho\u001b[0m\u001b[0;34m==\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m         \u001b[0mteacher\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m     \u001b[0;32melif\u001b[0m \u001b[0mwho\u001b[0m\u001b[0;34m==\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m         \u001b[0mstudent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-79-1034a3ab8d9f>\u001b[0m in \u001b[0;36mteacher\u001b[0;34m()\u001b[0m\n\u001b[1;32m     20\u001b[0m             \u001b[0mchoice\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Enter Your Choice: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mchoice\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m                 \u001b[0minsert\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     23\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m             \u001b[0;32melif\u001b[0m \u001b[0mchoice\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-71-832c744a5b7e>\u001b[0m in \u001b[0;36minsert\u001b[0;34m()\u001b[0m\n\u001b[1;32m      8\u001b[0m     \u001b[0mcursor\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcon\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcursor\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0msql\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"INSERT INTO student_detail (PROFILE, REG_NO, NAME, DEPARTMENT, CONTACT_NO, MAIL_ID) VALUES (%s, %s, %s, %s, %s, %s)\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m     \u001b[0mcursor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msql\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mimg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdept\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcontact\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmail\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m     \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mremove\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'{name}.jpg'\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# Remove the temporary file\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/mysql/connector/cursor_cext.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, operation, params, multi)\u001b[0m\n\u001b[1;32m    355\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    356\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 357\u001b[0;31m             result = self._connection.cmd_query(\n\u001b[0m\u001b[1;32m    358\u001b[0m                 \u001b[0mstmt\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    359\u001b[0m                 \u001b[0mraw\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_raw\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/mysql/connector/opentelemetry/context_propagation.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(cnx, *args, **kwargs)\u001b[0m\n\u001b[1;32m    104\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    105\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 106\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcnx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    107\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    108\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mtp_header\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/mysql/connector/connection_cext.py\u001b[0m in \u001b[0;36mcmd_query\u001b[0;34m(self, query, raw, buffered, raw_as_string)\u001b[0m\n\u001b[1;32m    712\u001b[0m             )\n\u001b[1;32m    713\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mMySQLInterfaceError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 714\u001b[0;31m             raise get_mysql_exception(\n\u001b[0m\u001b[1;32m    715\u001b[0m                 \u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merrno\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msqlstate\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msqlstate\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    716\u001b[0m             ) from err\n",
            "\u001b[0;31mIntegrityError\u001b[0m: 1048 (23000): Column 'PROFILE' cannot be null"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "gpuType": "T4",
      "provenance": [],
      "authorship_tag": "ABX9TyOcfeqNTU5k5qPCAsVAtCWh"
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}