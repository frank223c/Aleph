BEGIN;
--
-- Create model Autor
--
CREATE TABLE "Fondos_autor" ("id" serial NOT NULL PRIMARY KEY, "foto" varchar(100) NOT NULL, "alias" varchar(30) NOT NULL, "nombre" varchar(30) NOT NULL, "apellidos" varchar(40) NOT NULL, "procedencia" varchar(40) NOT NULL, "fnac" varchar(14) NOT NULL, "fdef" varchar(14) NOT NULL, "refbiografia" varchar(50) NOT NULL);
--
-- Create model Bibliografia
--
CREATE TABLE "Fondos_bibliografia" ("id" serial NOT NULL PRIMARY KEY, "autor" varchar(20) NOT NULL, "titulo" varchar(60) NOT NULL, "anio" varchar(30) NOT NULL, "pagina" varchar(30) NOT NULL, "edicion" varchar(10) NOT NULL, "extracto" text NOT NULL, "isbn" varchar(13) NOT NULL, "url" varchar(500) NOT NULL);
--
-- Create model Cultura
--
CREATE TABLE "Fondos_cultura" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL);
--
-- Create model Donante
--
CREATE TABLE "Fondos_donante" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL, "apellidos" varchar(30) NOT NULL, "dni" varchar(9) NOT NULL);
--
-- Create model Estudio
--
CREATE TABLE "Fondos_estudio" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(20) NOT NULL);
--
-- Create model Iconografia
--
CREATE TABLE "Fondos_iconografia" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL, "descripcion" text NOT NULL);
--
-- Create model InformeArqueo
--
CREATE TABLE "Fondos_informearqueo" ("id" serial NOT NULL PRIMARY KEY, "nombre_res" varchar(30) NOT NULL, "ape_res" varchar(50) NOT NULL, "proyecto" text NOT NULL, "observaciones" text NOT NULL, "desarrollo" text NOT NULL, "fecha" date NOT NULL);
--
-- Create model InformeEstado
--
CREATE TABLE "Fondos_informeestado" ("id" serial NOT NULL PRIMARY KEY, "nombre_res" varchar(30) NOT NULL, "ape_res" varchar(50) NOT NULL, "fecha" date NOT NULL, "cartela" text NOT NULL, "marco" text NOT NULL, "montaje" text NOT NULL, "muestras" boolean NOT NULL, "obra" text NOT NULL, "conclusion" text NOT NULL, "prioridad" integer NOT NULL, "propuesta" text NOT NULL, "metodologia" text NOT NULL);
--
-- Create model Material
--
CREATE TABLE "Fondos_material" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(20) NOT NULL);
--
-- Create model Movimiento
--
CREATE TABLE "Fondos_movimiento" ("id" serial NOT NULL PRIMARY KEY, "ciudad" varchar(20) NOT NULL, "museo" varchar(30) NOT NULL, "nombre_exposicion" varchar(30) NOT NULL, "fecha_prestado" date NOT NULL, "fecha_devuelto" date NOT NULL);
--
-- Create model Objeto
--
CREATE TABLE "Fondos_objeto" ("id" serial NOT NULL PRIMARY KEY, "anverso" varchar(100) NOT NULL, "reverso" varchar(100) NOT NULL, "codigo" varchar(2) NOT NULL, "numinv" integer NOT NULL UNIQUE, "altura" numeric(10, 2) NOT NULL, "ancho" numeric(10, 2) NOT NULL, "datacion" varchar(30) NOT NULL, "fechaingreso" varchar(30) NOT NULL, "ubicacionmus" varchar(30) NOT NULL, "descripcion" text NOT NULL, "observaciones" text NOT NULL);
--
-- Create model Seccion
--
CREATE TABLE "Fondos_seccion" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(10) NOT NULL);
--
-- Create model Serie
--
CREATE TABLE "Fondos_serie" 
("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(40) NOT NULL);
--
-- Create model Soporte
--
CREATE TABLE "Fondos_soporte" 
("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(10) NOT NULL);
--
-- Create model Tecnica
--
CREATE TABLE "Fondos_tecnica" 
("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL);
--
-- Create model Yacimiento
--
CREATE TABLE "Fondos_yacimiento" 
("id" serial NOT NULL PRIMARY KEY, "yacimiento" varchar(30) NOT NULL, "municipio" varchar(30) NOT NULL, "localidad" varchar(30) NOT NULL);
--
-- Create model Arqueologia
--
CREATE TABLE "Fondos_arqueologia" 
("objeto_ptr_id" integer NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL, "hallazgos" text NULL, "depositado" varchar(20) NOT NULL, "conservacion" varchar(1) NOT NULL, "edad" varchar(17) NOT NULL, "cultura_id" integer NOT NULL, "seccion_id" integer NULL, "serie_id" integer NOT NULL, "yacimiento_id" integer NOT NULL);

CREATE TABLE "Fondos_arqueologia_material" 
("id" serial NOT NULL PRIMARY KEY, "arqueologia_id" integer NOT NULL, "material_id" integer NOT NULL);
--
-- Create model Bellasartes
--
CREATE TABLE "Fondos_bellasartes" ("objeto_ptr_id" integer NOT NULL PRIMARY KEY, "titulo" varchar(40) NOT NULL, "procedencia" varchar(20) NOT NULL, "formaingreso" varchar(8) NOT NULL, "autor_id" integer NOT NULL, "donante_id" integer NULL, "iconografia_id" integer NOT NULL);
CREATE TABLE "Fondos_bellasartes_soporte" ("id" serial NOT NULL PRIMARY KEY, "bellasartes_id" integer NOT NULL, "soporte_id" integer NOT NULL);
CREATE TABLE "Fondos_bellasartes_tecnica" ("id" serial NOT NULL PRIMARY KEY, "bellasartes_id" integer NOT NULL, "tecnica_id" integer NOT NULL);
--
-- Create model InformeIntervencion
--
CREATE TABLE "Fondos_informeintervencion" ("estado_rel_id" integer NOT NULL PRIMARY KEY, "tipo" varchar(80) NOT NULL, "justificacion" text NOT NULL, "criterios" text NOT NULL, "estudios" boolean NOT NULL, "fecha" date NOT NULL, "priori_des" integer NOT NULL, "descripcioninter" text NOT NULL, "recom" text NOT NULL);
--
-- Add field bibliografia to objeto
--
CREATE TABLE "Fondos_objeto_bibliografia" ("id" serial NOT NULL PRIMARY KEY, "objeto_id" integer NOT NULL, "bibliografia_id" integer NOT NULL);
--
-- Add field movimientos to objeto
--
CREATE TABLE "Fondos_objeto_movimientos" ("id" serial NOT NULL PRIMARY KEY, "objeto_id" integer NOT NULL, "movimiento_id" integer NOT NULL);
--
-- Add field estudio to informeestado
--
CREATE TABLE "Fondos_informeestado_estudio" ("id" serial NOT NULL PRIMARY KEY, "informeestado_id" integer NOT NULL, "estudio_id" integer NOT NULL);
--
-- Add field objeto to informeestado
--
ALTER TABLE "Fondos_informeestado" ADD COLUMN "objeto_id" integer NOT NULL;
ALTER TABLE "Fondos_informeestado" ALTER COLUMN "objeto_id" DROP DEFAULT;
--
-- Add field objeto to informearqueo
--
ALTER TABLE "Fondos_informearqueo" ADD COLUMN "objeto_id" integer NOT NULL;
ALTER TABLE "Fondos_informearqueo" ALTER COLUMN "objeto_id" DROP DEFAULT;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_objeto_ptr_id_d35cef4a_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_ptr_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_cultura_id_229829e3_fk_Fondos_cultura_id" FOREIGN KEY ("cultura_id") REFERENCES "Fondos_cultura" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_seccion_id_30ec6ad1_fk_Fondos_seccion_id" FOREIGN KEY ("seccion_id") REFERENCES "Fondos_seccion" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_serie_id_a51b8fc6_fk_Fondos_serie_id" FOREIGN KEY ("serie_id") REFERENCES "Fondos_serie" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueolog_yacimiento_id_ca2ca21f_fk_Fondos_yacimiento_id" FOREIGN KEY ("yacimiento_id") REFERENCES "Fondos_yacimiento" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_arqueologia_c523cd6b" ON "Fondos_arqueologia" ("cultura_id");
CREATE INDEX "Fondos_arqueologia_9776281d" ON "Fondos_arqueologia" ("seccion_id");
CREATE INDEX "Fondos_arqueologia_c69a3c7b" ON "Fondos_arqueologia" ("serie_id");
CREATE INDEX "Fondos_arqueologia_385a4523" ON "Fondos_arqueologia" ("yacimiento_id");
ALTER TABLE "Fondos_arqueologia_material" ADD CONSTRAINT "Fon_arqueologia_id_a27a66cb_fk_Fondos_arqueologia_objeto_ptr_id" FOREIGN KEY ("arqueologia_id") REFERENCES "Fondos_arqueologia" ("objeto_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia_material" ADD CONSTRAINT "Fondos_arqueologia_m_material_id_c28995d0_fk_Fondos_material_id" FOREIGN KEY ("material_id") REFERENCES "Fondos_material" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia_material" ADD CONSTRAINT "Fondos_arqueologia_material_arqueologia_id_d85d6cf2_uniq" UNIQUE ("arqueologia_id", "material_id");
CREATE INDEX "Fondos_arqueologia_material_87305ea2" ON "Fondos_arqueologia_material" ("arqueologia_id");
CREATE INDEX "Fondos_arqueologia_material_eb4b9aaa" ON "Fondos_arqueologia_material" ("material_id");
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_objeto_ptr_id_8eee760d_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_ptr_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_autor_id_724f06a4_fk_Fondos_autor_id" FOREIGN KEY ("autor_id") REFERENCES "Fondos_autor" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_donante_id_75bc0401_fk_Fondos_donante_id" FOREIGN KEY ("donante_id") REFERENCES "Fondos_donante" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasa_iconografia_id_448ff3f8_fk_Fondos_iconografia_id" FOREIGN KEY ("iconografia_id") REFERENCES "Fondos_iconografia" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_bellasartes_52be3978" ON "Fondos_bellasartes" ("autor_id");
CREATE INDEX "Fondos_bellasartes_8b073f88" ON "Fondos_bellasartes" ("donante_id");
CREATE INDEX "Fondos_bellasartes_19f4d699" ON "Fondos_bellasartes" ("iconografia_id");
ALTER TABLE "Fondos_bellasartes_soporte" ADD CONSTRAINT "Fon_bellasartes_id_c62eafb7_fk_Fondos_bellasartes_objeto_ptr_id" FOREIGN KEY ("bellasartes_id") REFERENCES "Fondos_bellasartes" ("objeto_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_soporte" ADD CONSTRAINT "Fondos_bellasartes_sop_soporte_id_3e0ecdae_fk_Fondos_soporte_id" FOREIGN KEY ("soporte_id") REFERENCES "Fondos_soporte" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_soporte" ADD CONSTRAINT "Fondos_bellasartes_soporte_bellasartes_id_88f05bea_uniq" UNIQUE ("bellasartes_id", "soporte_id");
CREATE INDEX "Fondos_bellasartes_soporte_fd4b51fa" ON "Fondos_bellasartes_soporte" ("bellasartes_id");
CREATE INDEX "Fondos_bellasartes_soporte_3fdbe9ac" ON "Fondos_bellasartes_soporte" ("soporte_id");
ALTER TABLE "Fondos_bellasartes_tecnica" ADD CONSTRAINT "Fon_bellasartes_id_64a13e1e_fk_Fondos_bellasartes_objeto_ptr_id" FOREIGN KEY ("bellasartes_id") REFERENCES "Fondos_bellasartes" ("objeto_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_tecnica" ADD CONSTRAINT "Fondos_bellasartes_tec_tecnica_id_5ee71d3e_fk_Fondos_tecnica_id" FOREIGN KEY ("tecnica_id") REFERENCES "Fondos_tecnica" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_tecnica" ADD CONSTRAINT "Fondos_bellasartes_tecnica_bellasartes_id_ed7bba2a_uniq" UNIQUE ("bellasartes_id", "tecnica_id");
CREATE INDEX "Fondos_bellasartes_tecnica_fd4b51fa" ON "Fondos_bellasartes_tecnica" ("bellasartes_id");
CREATE INDEX "Fondos_bellasartes_tecnica_a7507e0d" ON "Fondos_bellasartes_tecnica" ("tecnica_id");
ALTER TABLE "Fondos_informeintervencion" ADD CONSTRAINT "Fondos_inform_estado_rel_id_ee1dff86_fk_Fondos_informeestado_id" FOREIGN KEY ("estado_rel_id") REFERENCES "Fondos_informeestado" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_bibliografia" ADD CONSTRAINT "Fondos_objeto_bibliograf_objeto_id_f5023d0f_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_bibliografia" ADD CONSTRAINT "Fondos_objet_bibliografia_id_afe2b682_fk_Fondos_bibliografia_id" FOREIGN KEY ("bibliografia_id") REFERENCES "Fondos_bibliografia" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_bibliografia" ADD CONSTRAINT "Fondos_objeto_bibliografia_objeto_id_c52a1000_uniq" UNIQUE ("objeto_id", "bibliografia_id");
CREATE INDEX "Fondos_objeto_bibliografia_251947c5" ON "Fondos_objeto_bibliografia" ("objeto_id");
CREATE INDEX "Fondos_objeto_bibliografia_074b8460" ON "Fondos_objeto_bibliografia" ("bibliografia_id");
ALTER TABLE "Fondos_objeto_movimientos" ADD CONSTRAINT "Fondos_objeto_movimiento_objeto_id_2e419ebd_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_movimientos" ADD CONSTRAINT "Fondos_objeto_mo_movimiento_id_5d9e2df3_fk_Fondos_movimiento_id" FOREIGN KEY ("movimiento_id") REFERENCES "Fondos_movimiento" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_movimientos" ADD CONSTRAINT "Fondos_objeto_movimientos_objeto_id_c060981e_uniq" UNIQUE ("objeto_id", "movimiento_id");
CREATE INDEX "Fondos_objeto_movimientos_251947c5" ON "Fondos_objeto_movimientos" ("objeto_id");
CREATE INDEX "Fondos_objeto_movimientos_b5630403" ON "Fondos_objeto_movimientos" ("movimiento_id");
ALTER TABLE "Fondos_informeestado_estudio" ADD CONSTRAINT "Fondos_inf_informeestado_id_8cc4530c_fk_Fondos_informeestado_id" FOREIGN KEY ("informeestado_id") REFERENCES "Fondos_informeestado" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_informeestado_estudio" ADD CONSTRAINT "Fondos_informeestado_e_estudio_id_b3a5be18_fk_Fondos_estudio_id" FOREIGN KEY ("estudio_id") REFERENCES "Fondos_estudio" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_informeestado_estudio" ADD CONSTRAINT "Fondos_informeestado_estudio_informeestado_id_6208624c_uniq" UNIQUE ("informeestado_id", "estudio_id");
CREATE INDEX "Fondos_informeestado_estudio_ff423109" ON "Fondos_informeestado_estudio" ("informeestado_id");
CREATE INDEX "Fondos_informeestado_estudio_11587e5e" ON "Fondos_informeestado_estudio" ("estudio_id");
CREATE INDEX "Fondos_informeestado_251947c5" ON "Fondos_informeestado" ("objeto_id");
ALTER TABLE "Fondos_informeestado" ADD CONSTRAINT "Fondos_informeestado_objeto_id_fd103e09_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_informearqueo_251947c5" ON "Fondos_informearqueo" ("objeto_id");
ALTER TABLE "Fondos_informearqueo" ADD CONSTRAINT "Fondos_informearqueo_objeto_id_3c2b25df_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
COMMIT;
