SQLite format 3   @     +   	   	                                                       + .O},  ��

��	�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ,�--�Ytabletbl_kursbelegungtbl_kursbelegungCREATE TABLE "tbl�--�Ytabletbl_kursbelegungtbl_kursbelegungCREATE TABLE "tbl_kursbelegung" (
    kurs_id INTEGER,
    student_id INTEGER,
    abiturfach INTEGER,
    punkte_12_1 INTEGER CHECK(0 <= punkte_12_1 <=15),
    punkte_12_2 INTEGER CHECK(0 <= punkte_12_2 <=15),
    punkte_13_1 INTEGER CHECK(0 <= punkte_13_1 <=15),
    punkte_13_2 INTEGER CHECK(0 <= punkte_13_2 <=15),
    punkte_pruefung INTEGER CHECK(0 <= punkte_pruefung <= 15),
    punkte_nachpruefung INTEGER CHECK(0 <= punkte_nachpruefung <=15),
    FOREIGN KEY (kurs_id) REFERENCES tbl_kurs(kurs_id),
    FOREIGN KEY (student_id) REFERENCES tbl_schueler(schueler_id),
    PRIMARY KEY(kurs_id, student_id)

)�A??�tabletbl_kursbelegung_templatetbl_kursbelegung_templateCREATE TABLE "tbl_kursbelegung_template" (
    template_name TEXT,
    kurs_id INTEGER,
    PRIMARY KEY (template_name, kurs_id)
)Qe? indexsqlite_autoindex_tbl_kursbelegung_template_1tbl_kursbelegung_template� �    �2//�tabletbl_kurs_belegungtbl_kurs_belegungCREATE TABLE "tbl_kurs_belegung" (
    kurs_belegung_id INTEGER PRIMARY�o%%�!tabletbl_schuelertbl_schuelerCREATE TABLE "tbl_schueler" (
    schueler_id INTEGER PRIMARY KEY,
    name TEXT,
    vorname TEXT,
    pflichtbindung BOOLEAN,
    wiederholung BOOLEAN,
    kurse_template INTEGER
, klasse TEXT)?S- indexsqlite_autoindex_tbl_kursbelegung_1tbl_kursbelegung     �)�%tabletbl_kurstbl_kursCREATE TABLE "tbl_kurs" (
    kurs_id INTEGER PRIMARY KEY,
    bezeichnung TEXT,
    aufgabenfeld INTEGER,
    abiturfach_kombi INTEGER,
    differenzierungskurs BOOLEAN,
    FOREIGN KEY (abiturfach_kombi) REFERENCES tbl_abiturfach_kombination(kombination_id)
)�AA�tabletbl_abiturfach_kombinationtbl_abiturfach_kombinationCREATE TABLE "tbl_abiturfach_kombination" (
    kombination_id INTEGER PRIMARY KEY,
    abiturfach_1 BOOLEAN,
    abiturfach_2 BOOLEAN,
    abiturfach_3 BOOLEAN,
    abiturfach_4 BOOLEAN
)   �%%�tabletbl_schuelertbl_schuelerCREATE TABLE "tbl_schueler" (
    schueler_id INTEGER PRIMARY KEY,
    name TEXT,
    vorname TEXT,
    pflichtbindung BOOLEAN,
    wiederholung BOOLEAN,
    kurse_template INTEGER
)   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     KajusLange   � ��������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          	 	 		 		 		 			 	   
���o��[<,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
 	Sport	 Physik 7Wirtschaftsinformatik !Mathematik =	Betriebswirtschaftslehre 7Volkswirtschaftslehre    1Gesellschaftslehre 	Deutsch 	Englisch 	Spanisch   
 ���������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

	       
	
	       	
	       
	       
	       
	       
	       
	       
	       

		          
� ����������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	
WG18C
		WG18C		WG18C	WG18C	WG18C	WG18C	WG18C	WG18C	WG18C	WG18C
   
� ����������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              WG18C

WG18C		WG18CWG18CWG18CWG18CWG18CWG18CWG18C			WG18C
   
� ����������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                	

													                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              