// Creating the student in 10 Students with attribute name and NIM.
CREATE (m1:Mahasiswa {Name:"Abdurrahman", NIM : "128"}),
        (m2:Mahasiswa {Name:"Miftahul", NIM : "127"}),
        (m3:Mahasiswa {Name:"Evan", NIM : "102"}),
        (m4:Mahasiswa {Name:"Fathir", NIM : "098"}),
        (m5:Mahasiswa {Name:"Raditia", NIM : "105"}),
        (m6:Mahasiswa {Name:"Nathanael", NIM : "107"}),
        (m7:Mahasiswa {Name:"Rangga", NIM : "106"}),
        (m8:Mahasiswa {Name:"Saiful", NIM : "115"}),
        (m9:Mahasiswa {Name:"Arsal", NIM : "111"}),
        (m10:Mahasiswa {Name:"Rafi", NIM : "143"});


//  Creating Mata Kuliah for each atribute name and prodi
CREATE (LMD:Matakuliah{name:"Logika Matematika Diskrit", prodi: "Sains Data", TPB : 4}),
        (ALPRO:Matakuliah{name:"Algoritma Pemrograman", prodi: "Teknik Informatika", TPB : 14}),
        (SSD:Matakuliah{name:"Statistika Sains Data", prodi: "Sains Data", TPB : 5}),
        (PEMWEB:Matakuliah{name:"Pemrograman Website", prodi: "Teknik Informatika", TPB:15}),
        (STRUKDAT:Matakuliah{name:"Struktur Data", prodi: "Sains Data", TPB : 2}),
        (MatDas:Matakuliah{name:"Matematika Dasar", prodi: "Teknik Lingkungan", TPB : 25}),
        (ADS:Matakuliah{name:"Analisis Data Statistik", prodi: "Sains Data", TPB:3}),
        (ANMUL:Matakuliah{name:"Analisis Multivariat", prodi: "Sains Data", TPB: 1}),
        (INTRANS:Matakuliah{name:"Infrastruktur dan Transportasi", prodi: "PWK", TPB:50}),
        (PM:Matakuliah{name:"Pembelajaran Mesin", prodi: "Sains Data", TPB: 56});

// Making Relationship between Mahasiswa and Matakuliah
CREATE 
  (m1:Mahasiswa {Name:"Abdurrahman", NIM:"128"})-[:MENGAMBIL]->(LMD:Matakuliah {name:"Logika Matematika Diskrit", prodi:"Sains Data", TPB:4}),
  (m2:Mahasiswa {Name:"Miftahul", NIM:"127"})-[:MENGAMBIL]->(ALPRO:Matakuliah {name:"Algoritma Pemrograman", prodi:"Teknik Informatika", TPB:14}),
  (m3:Mahasiswa {Name:"Evan", NIM:"102"})-[:MENGAMBIL]->(SSD:Matakuliah {name:"Statistika Sains Data", prodi:"Sains Data", TPB:5}),
  (m4:Mahasiswa {Name:"Fathir", NIM:"098"})-[:MENGAMBIL]->(PEMWEB:Matakuliah {name:"Pemrograman Website", prodi:"Teknik Informatika", TPB:15}),
  (m5:Mahasiswa {Name:"Raditia", NIM:"105"})-[:MENGAMBIL]->(STRUKDAT:Matakuliah {name:"Struktur Data", prodi:"Sains Data", TPB:2}),
  (m6:Mahasiswa {Name:"Nathanael", NIM:"107"})-[:MENGAMBIL]->(MatDas:Matakuliah {name:"Matematika Dasar", prodi:"Teknik Lingkungan", TPB:25}),
  (m7:Mahasiswa {Name:"Rangga", NIM:"106"})-[:MENGAMBIL]->(ADS:Matakuliah {name:"Analisis Data Statistik", prodi:"Sains Data", TPB:3}),
  (m8:Mahasiswa {Name:"Saiful", NIM:"115"})-[:MENGAMBIL]->(ANMUL:Matakuliah {name:"Analisis Multivariat", prodi:"Sains Data", TPB:1}),
  (m9:Mahasiswa {Name:"Arsal", NIM:"111"})-[:MENGAMBIL]->(INTRANS:Matakuliah {name:"Infrastruktur dan Transportasi", prodi:"PWK", TPB:50}),
  (m10:Mahasiswa {Name:"Rafi", NIM:"143"})-[:MENGAMBIL]->(PM:Matakuliah {name:"Pembelajaran Mesin", prodi:"Sains Data", TPB:56});


// Display the Node
MATCH (Mahasiswa)
return Mahasiswa;

MATCH (Matakuliah)
return Matakuliah;

// Change the Mahasiswa with other Nodes
MATCH (m:Mahasiswa)-[:MENGAMBIL]-> (mp:Matakuliah)
WHERE mp.name: "Statistika Sains Data"
RETURN m;

MATCH (m:Mahasiswa)-[:MENGAMBIL]-> (mp:Matakuliah{name:"Algoritma Pemrograman"})
RETURN m


// Remove all node and few node with return
MATCH (Mahasiswa)
DETACH DELETE Mahasiswa; 

