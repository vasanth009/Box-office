import pandas as pd
import mysql.connector
def datas_storing_database():
    view_data=pd.read_csv('movies_data.csv')
    print("\t\t\t\t\t\t****Movie Data's and Boxoffice Collection Details****\n\n",view_data)

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="datas_of_movies"
    )
    mycursor=mydb.cursor()
    print("\n\n\t\t\t\t\t\t****Now all the movie data's store in Database****")

#varisu movie data storing in database
    varisu_details=input("\nDo you want to store Varisu movie Data's in Database: ")
    if varisu_details=="yes":
        sql="insert into varisu_list(Movie, Hero, Heroin, Director, Music_director, Released_year, Budget, Boxoffice_collection) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        insert_datas=("Varisu", "Vijay", "Rashmika Mandana", "Vamshi", "Thaman", 2023, "170 crore", "310 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Varisu movie data's stored in database successfully***") 
    else:
        print("Varisu movie data's not stored in database..")

#Doctor movie data storing in database
    doctor_details=input("\nDo you want to store Doctor movie Data's in Database: ")
    if doctor_details=="yes":
        sql="insert into doctor_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Doctor","Sivakarthikeyan","Priyanka Mohan","Nelson","Anirudh",2021,"50 crore","100 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Doctor movie Data's stored in database successfully***")
    else:
        print("Doctor movie data's not stored in database..")

#Beast movie data storing in database
    beast_details=input("\nDo you want to store Beast movie Data's in Database: ")
    if beast_details=="yes":
        sql="insert into beast_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Beast","Vijay","Pooja Hegde","Nelson","Anirudh",2022,"150 crore","280 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Beast movie Data's stored in database successfully***")
    else:
        print("Beast movie data's not stored in database..")

#RRR movie data storing in database
    rrr_details=input("\nDo you want to store RRR movie Data's in Database: ")
    if rrr_details=="yes":
        sql="insert into rrr_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("RRR","Ram Charan","Alia bhat","SS.Rajamouli","Keeravani",2022,"350 crore","900 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***RRR movie Data's stored in database successfully***")
    else:
        print("RRR movie data's not stored in database..")

#Don movie data storing in database
    don_details=input("\nDo you want to store Don movie Data's in Database: ")
    if don_details=="yes":
        sql="insert into don_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Don","Sivakarthikeyan","Priyanka Mohan","Cibi Chakravarti","Anirudh",2022,"50 crore","130 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Don movie Data's stored in database successfully***")
    else:
        print("Don movie data's not stored in database..")

#Love today movie data storing in database 
    lovetoday_details=input("\nDo you want to store Love Today movie Data's in Database: ")
    if lovetoday_details=="yes":
        sql="insert into love_today_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Love Today","Pradeep","Ivana","Pradeep","Yuvan",2022,"10 crore","100 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Love Today movie Data's stored in database successfully***")
    else:
        print("Love Today movie data's not stored in database..") 

#Ayalaan movie data storing in database
    ayalaan_details=input("\nDo you want to store Ayalaan movie Data's in Database: ")
    if ayalaan_details=="yes":
        sql="insert into ayalaan_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Ayalaan","Sivakarthikeyan","Rakul preet sing","Ravikumar","A.R Rahman",2024,"70 crore","170 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Ayalaan movie Data's stored in database successfully***")
    else:
        print("ayalaan movie data's not stored in database..")

#captain miller movie data storing in database
    captain_miller_details=input("\nDo you want to store Captain Miller movie Data's in Database: ")
    if captain_miller_details=="yes":
        sql="insert into captain_miller_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Captain Miller","Dhanush","Priyanka Mohan","Arun","G.V Prakash",2024,"45 crore","120 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Captain miller movie Data's stored in database successfully***")
    else:
        print("Captain miller movie data's not stored in database..")

#KGF 2 movie data storing in database
    kgf2_details=input("\nDo you want to store KGF 2 movie Data's in Database: ")
    if kgf2_details=="yes":
        sql="insert into kgf2_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("KGF 2","Yash","Srinidhi Shetty","Prashant","Ravi Basrur",2022,"100 crore","800 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***KGF 2 movie Data's stored in database successfully***")
    else:
        print("KGF 2 movie data's not stored in database..")

#Aranmanai 4 movie data storing in database
    aranmanai4_details=input("\nDo you want to store Aranmanai 4 movie Data's in Database: ")
    if aranmanai4_details=="yes":
        sql="insert into aranmanai4_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Aranmanai 4","Sundar.C","Tamanna","Sundar.C","Hiphop Tamizha",2024,"40 crore","110 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Aranmanai 4 movie Data's stored in database successfully***")
    else:
        print("Aranmanai 4 movie data's not stored in database..")

#Devara movie data storing in database
    devara_details=input("\nDo you want to store Devara movie Data's in Database: ")
    if devara_details=="yes":
        sql="insert into devara_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Devara","NTR","Janhvi Kapoor","Koratala Siva","Anirudh",2024,"250 crore","460 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Devara movie Data's stored in database successfully***")
    else:
        print("Devara movie data's not stored in database..")

#Vettaiyan movie data storing in database
    vetaiyan_details=input("\nDo you want to store Vettaiyan movie Data's in Database: ")
    if vetaiyan_details=="yes":
        sql="insert into vettaiyan_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Vettaiyan","Rajini","Manju Warrior","Gnanavel","Anirudh",2024,"160 crore","450 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Vettaiyan movie Data's stored in database successfully***")
    else:
        print("Vettaiyan movie data's not stored in database..")

#ponniyin Selvan-2 movie data storing in database
    ponniyin_sel2_details=input("\nDo you want to store Ponniyin Selvan-2 movie Data's in Database: ")
    if ponniyin_sel2_details=="yes":
        sql="insert into ponniyin_sel2_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Ponniyin Selvan-2","Vikram","Aishwarya Rai","mani Ratnam","A.R Rahman",2022,"200 crore","400 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Ponniyin Selvan-2 movie Data's stored in database successfully***")
    else:
        print("Ponniyin Selvan-2 movie data's not stored in database..")

#Kanguva movie data storing in database
    kanguva_details=input("\nDo you want to store Kanguva movie Data's in Database: ")
    if kanguva_details=="yes":
        sql="insert into Kanguva_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Kanguva","Surya","Disha Patani","Siva","DSP",2024,"250 crore","430 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***kanguva movie Data's stored in database successfully***")
    else:
        print("Kanguva movie data's not stored in database..")

#Vidamuyarchi movie data storing in database
    vidamuyarchi_details=input("\nDo you want to store Vidamuyarchi movie Data's in Database: ")
    if vidamuyarchi_details=="yes":
        sql="insert into vidamuyarchi_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Vidamuyarchi","Ajith Kumar","Trisha","Magizh Thirumeni","Anirudh",2024,"150 croe","380 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Vidamuyarchi movie Data's stored in database successfully***")
    else:
        print("Vidamuyarchi movie data's not stored in database..")

#Indian 2 movie data storing in database
    indian2_details=input("\nDo you want to store Indian 2 movie Data's in Database: ")
    if indian2_details=="yes":
        sql="insert into indian2_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Indian 2","Kamal Hasan","Kajal Agarwal","Shankar","Anirudh",2024,"200 crore","500 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Indian 2 movie Data's stored in database successfully***")
    else:
        print("Indian 2 movie data's not stored in database..")

#GOAT movie data storing in database
    Goat_details=input("\nDo you want to store GOAT movie Data's in Database: ")
    if Goat_details=="yes":
        sql="insert into Goat_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("GOAT","Vijay","Meenakshi","Venkat Prabu","Yuvan",2024,"150 crore","350 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***GOAT movie Data's stored in database successfully***")
    else:
        print("GOAT movie data's not stored in database..")

#Kalki movie data storing in database
    kalki_details=input("\nDo you want to store Kalki movie Data's in Database: ")
    if kalki_details=="yes":
        sql="insert into kalki_details(Movie,Hero,Heroin,Director,Music_director,Released_year,Budget,Boxoffice_collection) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_datas=("Kalki","Prabhas","Disha patani","Nag Ashwin","Santhosh Narayanan",2024,"300 crore","800 crore")
        mycursor.execute(sql,insert_datas)
        mydb.commit()
        print("***Kalki movie Data's stored in database successfully***")
    else:
        print("Kalki movie data's not stored in database..")

#printing all movie data's from database
    print("\n\t\t\t\t\t\t***Now showing all movie data's from database***")

#taking varisu movie data
    if input("\nDo you want to show varisu movie Data's from database: ") == "yes":
        mycursor.execute("select * from varisu_list")
        print(*mycursor.fetchall(), sep='\n')

#taking doctor movie data
    if input("\nDo you want to show Doctor movie Data's from database: ") == "yes":
        mycursor.execute("select * from doctor_details")
        print(*mycursor.fetchall(), sep='\n')

#taking beast movie data
    if input("\nDo you want to show Beast movie Data's from database: ") == "yes":
        mycursor.execute("select * from beast_details")
        print(*mycursor.fetchall(), sep='\n')

#taking rrr movie data
    if input("\nDo you want to show RRR movie Data's from database: ") == "yes":
        mycursor.execute("select * from rrr_details")
        print(*mycursor.fetchall(), sep='\n')

#taking don movie data
    if input("\nDo you want to show Don movie Data's from database: ") == "yes":
        mycursor.execute("select * from don_details")
        print(*mycursor.fetchall(), sep='\n')

#taking love today movie data
    if input("\nDo you want to show Love Today movie Data's from database: ") == "yes":
        mycursor.execute("select * from love_today_details")
        print(*mycursor.fetchall(), sep='\n')

#taking ayalaan movie data
    if input("\nDo you want to show ayalaan movie Data's from database: ") == "yes":
        mycursor.execute("select * from ayalaan_details")
        print(*mycursor.fetchall(), sep='\n')

#taking captain miller movie data
    if input("\nDo you want to show Captain Miller movie Data's from database: ") == "yes":
        mycursor.execute("select * from captain_miller_details")
        print(*mycursor.fetchall(), sep='\n')

#taking kgf2 movie data
    if input("\nDo you want to show KGF 2 movie Data's from database: ") == "yes":
        mycursor.execute("select * from kgf2_details")
        print(*mycursor.fetchall(), sep='\n')

#taking Aranmanai 4 movie data
    if input("\nDo you want to show aranmanai 4 movie Data's from database: ") == "yes":
        mycursor.execute("select * from aranmanai4_details")
        print(*mycursor.fetchall(), sep='\n')

#taking devara movie data
    if input("\nDo you want to show Devara movie Data's from database: ") == "yes":
        mycursor.execute("select * from devara_details")
        print(*mycursor.fetchall(), sep='\n')

#taking vettaiyan movie data
    if input("\nDo you want to show Vettaiyan movie Data's from database: ") == "yes":
        mycursor.execute("select * from vettaiyan_details")
        print(*mycursor.fetchall(), sep='\n')

#taking ponniyin selvan movie data
    if input("\nDo you want to show Ponniyin Selvan 2 movie Data's from database: ") == "yes":
        mycursor.execute("select * from ponniyin_sel2_details")
        print(*mycursor.fetchall(), sep='\n')

#taking kanguva movie data
    if input("\nDo you want to show Kanguva movie Data's from database: ") == "yes":
        mycursor.execute("select * from kanguva_details")
        print(*mycursor.fetchall(), sep='\n')

#taking vidamuyarchi movie data
    if input("\nDo you want to show Vidamuyarchi movie Data's from database: ") == "yes":
        mycursor.execute("select * from vidamuyarchi_details")
        print(*mycursor.fetchall(), sep='\n')

#taking indian 2 movie data
    if input("\nDo you want to show Indian 2 movie Data's from database: ") == "yes":
        mycursor.execute("select * from indian2_details")
        print(*mycursor.fetchall(), sep='\n')

#taking GOAT movie data
    if input("\nDo you want to show GOAT movie Data's from database: ") == "yes":
        mycursor.execute("select * from goat_details")
        print(*mycursor.fetchall(), sep='\n')
        
#taking kalki movie data
    if input("\nDo you want to show Kalki movie Data's from database: ") == "yes":
        mycursor.execute("select * from kalki_details")
        print(*mycursor.fetchall(), sep='\n')

#calling function
datas_storing_database()
