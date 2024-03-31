-- Trigger postgis
create extension if not exists postgis;
create extension if not exists postgis_topology;

-- Mengecek versi dari postgis 
select postgis_version() 


-- Soal 1 : Titik Sudut 
-- Membuat tabel spasial 
create table abdurrahman_netherlands(
	id serial primary key,
	tujuan_wisata varchar(100),
	lokasi geometry(point, 4326)
)

-- Masukan data kedalam tabel
insert into abdurrahman_netherlands(tujuan_wisata, lokasi)
values
	('Amsterdam', ST_GeomFromText('point(4.9004515566675035 52.36641588558316)', 4326)),
	('Ruigoord', ST_GeomFromText('point(4.749431201086546 52.41102153629598)', 4326)),
	('Muiden', ST_GeomFromText('point(5.067531905068999 52.328918613289545)', 4326)),
	('Abcoude', ST_GeomFromText('point(4.9713001524276885 52.271775095828254)', 4326)),
	('Wilnis', ST_GeomFromText('point(4.907357118700586 52.19433047247097)', 4326)),
	('Zegveld', ST_GeomFromText('point(4.841802207150338 52.11236928004155)', 4326)),
	('Bodegraven', ST_GeomFromText('point(4.739488929787247 52.082696664463995)', 4326)),
	('Boskoop', ST_GeomFromText('point(4.65409268786447 52.07479539581394)', 4326)),
	('Rotterdam', ST_GeomFromText('point(4.46740576795244 51.92333975871206)', 4326)),
	('Den Haag', ST_GeomFromText('point(4.303612410481544 52.070820801924555)', 4326));
	
-- Memilih data yang sudah dibuat 
select  * from abdurrahman_netherlands;


-- Soal 2 : Polygon
-- Membuat tabel batas daerah 
create table abdurrahman_amsterdam (
	id serial PRIMARY KEY,
	nama_kota varchar(100),
	batas_kota GEOMETRY(POLYGON, 4326)
);

-- Masukan insert data batas daerah 
INSERT INTO abdurrahman_amsterdam (nama_kota, batas_kota)
VALUES
	('Amsterdam', ST_GeomFromText('POLYGON((4.738540 52.430175, 4.853206 52.415069, 4.866791 52.431393, 4.983454 52.427008, 5.068842 52.415558, 5.009221 52.372860, 5.031235 52.352124, 5.002042 52.343061, 4.964714 52.353001, 4.913627 52.328636, 4.910756 52.317520, 4.855720 52.321323, 4.756656 52.357873, 4.757613 52.396729, 4.728420 52.399649, 4.738540 52.430175))', 4326));

select * from abdurrahman_amsterdam;


-- Soal 3 : Titik Perjalanan
create table abdurrahman_perjalanan(
	id SERIAL primary key,
	nama_tujuan VARCHAR(100), -- nama perjalanan
	waktu TIMESTAMP, -- Waktu titik diperoleh
	lokasi GEOMETRY(Point, 4326) -- koor titik (SERIALRID WGS 84)
);

INSERT INTO abdurrahman_perjalanan (nama_tujuan, waktu, lokasi) VALUES
	('Foam', '2024-03-17 08:00:00', ST_GeomFromText('POINT(4.893017 52.364342)', 4326)),
	('Foam', '2024-03-17 08:01:00', ST_GeomFromText('POINT(4.894874 52.363936)', 4326)),
	('Foam', '2024-03-17 08:02:00', ST_GeomFromText('POINT(4.897447 52.364351)', 4326)),
	('Foam', '2024-03-17 08:03:00', ST_GeomFromText('POINT(4.900217 52.364686)', 4326)),
	('Foam', '2024-03-17 08:04:00', ST_GeomFromText('POINT(4.901863 52.364753)', 4326)),
	('Foam', '2024-03-17 08:05:00', ST_GeomFromText('POINT(4.903179 52.365239)', 4326)),
	('Hart Museum', '2024-03-17 09:01:00', ST_GeomFromText('POINT(4.893017 52.364342)', 4326)),
	('Hart Museum', '2024-03-17 08:02:00', ST_GeomFromText('POINT(4.901369 52.365289)', 4326)),
	('Hart Museum', '2024-03-17 09:03:00', ST_GeomFromText('POINT(4.900245 52.365155)', 4326)),
	('Hart Museum', '2024-03-17 09:04:00', ST_GeomFromText('POINT(4.897255 52.364686)', 4326)),
	('Hart Museum', '2024-03-17 09:05:00', ST_GeomFromText('POINT(4.895609 52.364519)', 4326)),
	('Hart Museum', '2024-03-17 09:06:00', ST_GeomFromText('POINT(4.893470 52.364686)', 4326));


select * from abdurrahman_perjalanan;

-- Pembuatan Data Spasial
select nama_tujuan, st_makeline(lokasi order by waktu) as travel_path
from abdurrahman_perjalanan
group by nama_tujuan;
