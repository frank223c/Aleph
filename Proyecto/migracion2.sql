
--
-- Create model Autor
--
CREATE TABLE "Fondos_autor" ("id" serial NOT NULL PRIMARY KEY, "foto" varchar(100) NOT NULL, "alias" varchar(30) NOT NULL, "nombre" varchar(30) NOT NULL, "apellidos" varchar(60) NOT NULL, "fnac" varchar(14) NOT NULL, "fdef" varchar(14) NOT NULL);
--
-- Create model Bibliografia
--
CREATE TABLE "Fondos_bibliografia" ("id" serial NOT NULL PRIMARY KEY, "titulo" varchar(60) NOT NULL, "pagina" varchar(30) NOT NULL, "edicion" varchar(10) NOT NULL, "extracto" text NOT NULL);
--
-- Create model Ca
--
CREATE TABLE "Fondos_ca" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(20) NOT NULL);
--
-- Create model Continente
--
CREATE TABLE "Fondos_continente" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(40) NOT NULL);
--
-- Create model Cultura
--
CREATE TABLE "Fondos_cultura" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL);
--
-- Create model Donante
--
CREATE TABLE "Fondos_donante" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(60) NOT NULL, "apellidos" varchar(60) NOT NULL);
--
-- Create model Escritor
--
CREATE TABLE "Fondos_escritor" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(60) NOT NULL, "apellidos" varchar(60) NOT NULL);
--
-- Create model Estudio
--
CREATE TABLE "Fondos_estudio" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(20) NOT NULL);
--
-- Create model Exposicion
--
CREATE TABLE "Fondos_exposicion" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL);
--
-- Create model Iconografia
--
CREATE TABLE "Fondos_iconografia" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL);
--
-- Create model InformeArqueo
--
CREATE TABLE "Fondos_informearqueo" ("id" serial NOT NULL PRIMARY KEY, "nombre_res" varchar(30) NOT NULL, "ape_res" varchar(50) NOT NULL, "diagnostico" text NOT NULL, "proyecto" text NOT NULL, "desarrollo" text NOT NULL, "fecha" date NOT NULL);
--
-- Create model InformeEstado
--
CREATE TABLE "Fondos_informeestado" ("id" serial NOT NULL PRIMARY KEY, "nombre_res" varchar(30) NOT NULL, "ape_res" varchar(50) NOT NULL, "fecha" date NOT NULL, "cartela" text NOT NULL, "marco" text NOT NULL, "obra" text NOT NULL, "prioridad" integer NOT NULL, "propuesta" text NOT NULL);
--
-- Create model Material
--
CREATE TABLE "Fondos_material" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(20) NOT NULL);
--
-- Create model Movimiento
--
CREATE TABLE "Fondos_movimiento" ("id" serial NOT NULL PRIMARY KEY, "fecha_prestado" date NOT NULL, "fecha_devuelto" date NOT NULL, "expo_id" integer NOT NULL);
--
-- Create model Municipio
--
CREATE TABLE "Fondos_municipio" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(20) NOT NULL);
--
-- Create model Museo
--
CREATE TABLE "Fondos_museo" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL, "ciudad_id" integer NOT NULL);
--
-- Create model Objeto
--
CREATE TABLE "Fondos_objeto" ("id" serial NOT NULL PRIMARY KEY, "anverso" varchar(100) NOT NULL, "reverso" varchar(100) NOT NULL, "codigo" varchar(2) NOT NULL, "numinv" integer NOT NULL UNIQUE, "altura" numeric(10, 2) NOT NULL, "ancho" numeric(10, 2) NOT NULL, "datacion" varchar(30) NOT NULL, "fechaingreso" date NOT NULL, "numero_entrada" integer NOT NULL, "descripcion" text NOT NULL, "observaciones" text NOT NULL);
--
-- Create model Pais
--
CREATE TABLE "Fondos_pais" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(40) NOT NULL, "continente_id" integer NOT NULL);
--
-- Create model Provincia
--
CREATE TABLE "Fondos_provincia" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(20) NOT NULL, "ca_id" integer NOT NULL);
--
-- Create model Seccion
--
CREATE TABLE "Fondos_seccion" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(10) NOT NULL);
--
-- Create model Serie
--
CREATE TABLE "Fondos_serie" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(40) NOT NULL);
--
-- Create model Soporte
--
CREATE TABLE "Fondos_soporte" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(10) NOT NULL);
--
-- Create model Tecnica
--
CREATE TABLE "Fondos_tecnica" ("id" serial NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL);
--
-- Create model Ubicacion
--
CREATE TABLE "Fondos_ubicacion" ("id" serial NOT NULL PRIMARY KEY, "tipo" varchar(10) NOT NULL, "nombre" varchar(20) NOT NULL);
--
-- Create model Yacimiento
--
CREATE TABLE "Fondos_yacimiento" ("id" serial NOT NULL PRIMARY KEY, "yacimiento" varchar(30) NOT NULL, "municipio_id" integer NOT NULL);
--
-- Create model Arqueologia
--
CREATE TABLE "Fondos_arqueologia" ("objeto_ptr_id" integer NOT NULL PRIMARY KEY, "nombre" varchar(30) NOT NULL, "hallazgos" text NOT NULL, "depositado" varchar(20) NOT NULL, "conservacion" varchar(1) NOT NULL, "edad" varchar(17) NOT NULL, "cultura_id" integer NULL, "seccion_id" integer NOT NULL, "serie_id" integer NOT NULL, "yacimiento_id" integer NOT NULL);
CREATE TABLE "Fondos_arqueologia_material" ("id" serial NOT NULL PRIMARY KEY, "arqueologia_id" integer NOT NULL, "material_id" integer NOT NULL);
--
-- Create model Bellasartes
--
CREATE TABLE "Fondos_bellasartes" ("objeto_ptr_id" integer NOT NULL PRIMARY KEY, "titulo" varchar(100) NOT NULL, "formaingreso" varchar(8) NOT NULL);
--
-- Create model InformeIntervencion
--
CREATE TABLE "Fondos_informeintervencion" ("estado_rel_id" integer NOT NULL PRIMARY KEY, "tipo" varchar(80) NOT NULL, "justificacion" text NOT NULL, "criterios" text NOT NULL, "estudios" boolean NOT NULL, "fecha" date NOT NULL, "descripcioninter" text NOT NULL, "recom" text NOT NULL, "priori_des" integer NOT NULL);
--
-- Add field bibliografia to objeto
--
CREATE TABLE "Fondos_objeto_bibliografia" ("id" serial NOT NULL PRIMARY KEY, "objeto_id" integer NOT NULL, "bibliografia_id" integer NOT NULL);
--
-- Add field ubicacion to objeto
--
ALTER TABLE "Fondos_objeto" ADD COLUMN "ubicacion_id" integer DEFAULT 1 NOT NULL;
ALTER TABLE "Fondos_objeto" ALTER COLUMN "ubicacion_id" DROP DEFAULT;
--
-- Add field provincia to municipio
--
ALTER TABLE "Fondos_municipio" ADD COLUMN "provincia_id" integer NOT NULL;
--
-- Add field estudio to informeestado
--
CREATE TABLE "Fondos_informeestado_estudio" ("id" serial NOT NULL PRIMARY KEY, "informeestado_id" integer NOT NULL, "estudio_id" integer NOT NULL);
--
-- Add field objeto to informeestado
--
ALTER TABLE "Fondos_informeestado" ADD COLUMN "objeto_id" integer NOT NULL;
--
-- Add field objeto to informearqueo
--
ALTER TABLE "Fondos_informearqueo" ADD COLUMN "objeto_id" integer NOT NULL;
--
-- Add field museo to exposicion
--
ALTER TABLE "Fondos_exposicion" ADD COLUMN "museo_id" integer NOT NULL;
--
-- Add field pais to ca
--
ALTER TABLE "Fondos_ca" ADD COLUMN "pais_id" integer NOT NULL;
--
-- Add field autor to bibliografia
--
ALTER TABLE "Fondos_bibliografia" ADD COLUMN "autor_id" integer NOT NULL;
--
-- Add field procedencia to autor
--
ALTER TABLE "Fondos_autor" ADD COLUMN "procedencia_id" integer NOT NULL;
--
-- Add field objeto to movimiento
--
ALTER TABLE "Fondos_movimiento" ADD COLUMN "objeto_id" integer NOT NULL;
--
-- Add field autor to bellasartes
--
ALTER TABLE "Fondos_bellasartes" ADD COLUMN "autor_id" integer NULL;
--
-- Add field donante to bellasartes
--
ALTER TABLE "Fondos_bellasartes" ADD COLUMN "donante_id" integer NULL;
--
-- Add field iconografia to bellasartes
--
CREATE TABLE "Fondos_bellasartes_iconografia" ("id" serial NOT NULL PRIMARY KEY, "bellasartes_id" integer NOT NULL, "iconografia_id" integer NOT NULL);
--
-- Add field procedencia to bellasartes
--
ALTER TABLE "Fondos_bellasartes" ADD COLUMN "procedencia_id" integer NOT NULL;
--
-- Add field produ to bellasartes
--
ALTER TABLE "Fondos_bellasartes" ADD COLUMN "produ_id" integer NOT NULL;
--
-- Add field soporte to bellasartes
--
ALTER TABLE "Fondos_bellasartes" ADD COLUMN "soporte_id" integer NOT NULL;
--
-- Add field tecnica to bellasartes
--
CREATE TABLE "Fondos_bellasartes_tecnica" ("id" serial NOT NULL PRIMARY KEY, "bellasartes_id" integer NOT NULL, "tecnica_id" integer NOT NULL);
ALTER TABLE "Fondos_movimiento" ADD CONSTRAINT "Fondos_movimiento_expo_id_15d6d3a5_fk_Fondos_exposicion_id" FOREIGN KEY ("expo_id") REFERENCES "Fondos_exposicion" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_movimiento_expo_id_15d6d3a5" ON "Fondos_movimiento" ("expo_id");
ALTER TABLE "Fondos_museo" ADD CONSTRAINT "Fondos_museo_ciudad_id_5a24c3a5_fk_Fondos_municipio_id" FOREIGN KEY ("ciudad_id") REFERENCES "Fondos_municipio" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_museo_ciudad_id_5a24c3a5" ON "Fondos_museo" ("ciudad_id");
ALTER TABLE "Fondos_pais" ADD CONSTRAINT "Fondos_pais_continente_id_e2bfcf63_fk_Fondos_continente_id" FOREIGN KEY ("continente_id") REFERENCES "Fondos_continente" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_pais_continente_id_e2bfcf63" ON "Fondos_pais" ("continente_id");
ALTER TABLE "Fondos_provincia" ADD CONSTRAINT "Fondos_provincia_ca_id_bd1560cf_fk_Fondos_ca_id" FOREIGN KEY ("ca_id") REFERENCES "Fondos_ca" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_provincia_ca_id_bd1560cf" ON "Fondos_provincia" ("ca_id");
ALTER TABLE "Fondos_yacimiento" ADD CONSTRAINT "Fondos_yacimiento_municipio_id_dbcabe49_fk_Fondos_municipio_id" FOREIGN KEY ("municipio_id") REFERENCES "Fondos_municipio" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_yacimiento_municipio_id_dbcabe49" ON "Fondos_yacimiento" ("municipio_id");
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_objeto_ptr_id_d35cef4a_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_ptr_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_cultura_id_229829e3_fk_Fondos_cultura_id" FOREIGN KEY ("cultura_id") REFERENCES "Fondos_cultura" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_seccion_id_30ec6ad1_fk_Fondos_seccion_id" FOREIGN KEY ("seccion_id") REFERENCES "Fondos_seccion" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_serie_id_a51b8fc6_fk_Fondos_serie_id" FOREIGN KEY ("serie_id") REFERENCES "Fondos_serie" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia" ADD CONSTRAINT "Fondos_arqueologia_yacimiento_id_ca2ca21f_fk_Fondos_ya" FOREIGN KEY ("yacimiento_id") REFERENCES "Fondos_yacimiento" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_arqueologia_cultura_id_229829e3" ON "Fondos_arqueologia" ("cultura_id");
CREATE INDEX "Fondos_arqueologia_seccion_id_30ec6ad1" ON "Fondos_arqueologia" ("seccion_id");
CREATE INDEX "Fondos_arqueologia_serie_id_a51b8fc6" ON "Fondos_arqueologia" ("serie_id");
CREATE INDEX "Fondos_arqueologia_yacimiento_id_ca2ca21f" ON "Fondos_arqueologia" ("yacimiento_id");
ALTER TABLE "Fondos_arqueologia_material" ADD CONSTRAINT "Fondos_arqueologia_m_arqueologia_id_a27a66cb_fk_Fondos_ar" FOREIGN KEY ("arqueologia_id") REFERENCES "Fondos_arqueologia" ("objeto_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia_material" ADD CONSTRAINT "Fondos_arqueologia_m_material_id_c28995d0_fk_Fondos_ma" FOREIGN KEY ("material_id") REFERENCES "Fondos_material" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_arqueologia_material" ADD CONSTRAINT "Fondos_arqueologia_mater_arqueologia_id_material__d85d6cf2_uniq" UNIQUE ("arqueologia_id", "material_id");
CREATE INDEX "Fondos_arqueologia_material_arqueologia_id_a27a66cb" ON "Fondos_arqueologia_material" ("arqueologia_id");
CREATE INDEX "Fondos_arqueologia_material_material_id_c28995d0" ON "Fondos_arqueologia_material" ("material_id");
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_objeto_ptr_id_8eee760d_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_ptr_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_informeintervencion" ADD CONSTRAINT "Fondos_informeinterv_estado_rel_id_ee1dff86_fk_Fondos_in" FOREIGN KEY ("estado_rel_id") REFERENCES "Fondos_informeestado" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_bibliografia" ADD CONSTRAINT "Fondos_objeto_biblio_objeto_id_f5023d0f_fk_Fondos_ob" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_bibliografia" ADD CONSTRAINT "Fondos_objeto_biblio_bibliografia_id_afe2b682_fk_Fondos_bi" FOREIGN KEY ("bibliografia_id") REFERENCES "Fondos_bibliografia" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_objeto_bibliografia" ADD CONSTRAINT "Fondos_objeto_bibliograf_objeto_id_bibliografia_i_c52a1000_uniq" UNIQUE ("objeto_id", "bibliografia_id");
CREATE INDEX "Fondos_objeto_bibliografia_objeto_id_f5023d0f" ON "Fondos_objeto_bibliografia" ("objeto_id");
CREATE INDEX "Fondos_objeto_bibliografia_bibliografia_id_afe2b682" ON "Fondos_objeto_bibliografia" ("bibliografia_id");
CREATE INDEX "Fondos_objeto_ubicacion_id_4108da1a" ON "Fondos_objeto" ("ubicacion_id");
ALTER TABLE "Fondos_objeto" ADD CONSTRAINT "Fondos_objeto_ubicacion_id_4108da1a_fk_Fondos_ubicacion_id" FOREIGN KEY ("ubicacion_id") REFERENCES "Fondos_ubicacion" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_municipio_provincia_id_792bd794" ON "Fondos_municipio" ("provincia_id");
ALTER TABLE "Fondos_municipio" ADD CONSTRAINT "Fondos_municipio_provincia_id_792bd794_fk_Fondos_provincia_id" FOREIGN KEY ("provincia_id") REFERENCES "Fondos_provincia" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_informeestado_estudio" ADD CONSTRAINT "Fondos_informeestado_informeestado_id_8cc4530c_fk_Fondos_in" FOREIGN KEY ("informeestado_id") REFERENCES "Fondos_informeestado" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_informeestado_estudio" ADD CONSTRAINT "Fondos_informeestado_estudio_id_b3a5be18_fk_Fondos_es" FOREIGN KEY ("estudio_id") REFERENCES "Fondos_estudio" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_informeestado_estudio" ADD CONSTRAINT "Fondos_informeestado_est_informeestado_id_estudio_6208624c_uniq" UNIQUE ("informeestado_id", "estudio_id");
CREATE INDEX "Fondos_informeestado_estudio_informeestado_id_8cc4530c" ON "Fondos_informeestado_estudio" ("informeestado_id");
CREATE INDEX "Fondos_informeestado_estudio_estudio_id_b3a5be18" ON "Fondos_informeestado_estudio" ("estudio_id");
CREATE INDEX "Fondos_informeestado_objeto_id_fd103e09" ON "Fondos_informeestado" ("objeto_id");
ALTER TABLE "Fondos_informeestado" ADD CONSTRAINT "Fondos_informeestado_objeto_id_fd103e09_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_informearqueo_objeto_id_3c2b25df" ON "Fondos_informearqueo" ("objeto_id");
ALTER TABLE "Fondos_informearqueo" ADD CONSTRAINT "Fondos_informearqueo_objeto_id_3c2b25df_fk_Fondos_objeto_id" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_objeto" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_exposicion_museo_id_c7607ff2" ON "Fondos_exposicion" ("museo_id");
ALTER TABLE "Fondos_exposicion" ADD CONSTRAINT "Fondos_exposicion_museo_id_c7607ff2_fk_Fondos_museo_id" FOREIGN KEY ("museo_id") REFERENCES "Fondos_museo" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_ca_pais_id_462f0828" ON "Fondos_ca" ("pais_id");
ALTER TABLE "Fondos_ca" ADD CONSTRAINT "Fondos_ca_pais_id_462f0828_fk_Fondos_pais_id" FOREIGN KEY ("pais_id") REFERENCES "Fondos_pais" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_bibliografia_autor_id_e6e995de" ON "Fondos_bibliografia" ("autor_id");
ALTER TABLE "Fondos_bibliografia" ADD CONSTRAINT "Fondos_bibliografia_autor_id_e6e995de_fk_Fondos_escritor_id" FOREIGN KEY ("autor_id") REFERENCES "Fondos_escritor" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_autor_procedencia_id_1d684419" ON "Fondos_autor" ("procedencia_id");
ALTER TABLE "Fondos_autor" ADD CONSTRAINT "Fondos_autor_procedencia_id_1d684419_fk_Fondos_pais_id" FOREIGN KEY ("procedencia_id") REFERENCES "Fondos_pais" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_movimiento_objeto_id_2883ff85" ON "Fondos_movimiento" ("objeto_id");
ALTER TABLE "Fondos_movimiento" ADD CONSTRAINT "Fondos_movimiento_objeto_id_2883ff85_fk_Fondos_be" FOREIGN KEY ("objeto_id") REFERENCES "Fondos_bellasartes" ("objeto_ptr_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_bellasartes_autor_id_724f06a4" ON "Fondos_bellasartes" ("autor_id");
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_autor_id_724f06a4_fk_Fondos_autor_id" FOREIGN KEY ("autor_id") REFERENCES "Fondos_autor" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_bellasartes_donante_id_75bc0401" ON "Fondos_bellasartes" ("donante_id");
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_donante_id_75bc0401_fk_Fondos_donante_id" FOREIGN KEY ("donante_id") REFERENCES "Fondos_donante" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_iconografia" ADD CONSTRAINT "Fondos_bellasartes_i_bellasartes_id_73d8143b_fk_Fondos_be" FOREIGN KEY ("bellasartes_id") REFERENCES "Fondos_bellasartes" ("objeto_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_iconografia" ADD CONSTRAINT "Fondos_bellasartes_i_iconografia_id_141d9a74_fk_Fondos_ic" FOREIGN KEY ("iconografia_id") REFERENCES "Fondos_iconografia" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_iconografia" ADD CONSTRAINT "Fondos_bellasartes_icono_bellasartes_id_iconograf_ac5e24dd_uniq" UNIQUE ("bellasartes_id", "iconografia_id");
CREATE INDEX "Fondos_bellasartes_iconografia_bellasartes_id_73d8143b" ON "Fondos_bellasartes_iconografia" ("bellasartes_id");
CREATE INDEX "Fondos_bellasartes_iconografia_iconografia_id_141d9a74" ON "Fondos_bellasartes_iconografia" ("iconografia_id");
CREATE INDEX "Fondos_bellasartes_procedencia_id_3be312bb" ON "Fondos_bellasartes" ("procedencia_id");
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_procedencia_id_3be312bb_fk_Fondos_ya" FOREIGN KEY ("procedencia_id") REFERENCES "Fondos_yacimiento" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_bellasartes_produ_id_4bfa9d63" ON "Fondos_bellasartes" ("produ_id");
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_produ_id_4bfa9d63_fk_Fondos_pais_id" FOREIGN KEY ("produ_id") REFERENCES "Fondos_pais" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "Fondos_bellasartes_soporte_id_f76a0275" ON "Fondos_bellasartes" ("soporte_id");
ALTER TABLE "Fondos_bellasartes" ADD CONSTRAINT "Fondos_bellasartes_soporte_id_f76a0275_fk_Fondos_soporte_id" FOREIGN KEY ("soporte_id") REFERENCES "Fondos_soporte" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_tecnica" ADD CONSTRAINT "Fondos_bellasartes_t_bellasartes_id_64a13e1e_fk_Fondos_be" FOREIGN KEY ("bellasartes_id") REFERENCES "Fondos_bellasartes" ("objeto_ptr_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_tecnica" ADD CONSTRAINT "Fondos_bellasartes_t_tecnica_id_5ee71d3e_fk_Fondos_te" FOREIGN KEY ("tecnica_id") REFERENCES "Fondos_tecnica" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "Fondos_bellasartes_tecnica" ADD CONSTRAINT "Fondos_bellasartes_tecni_bellasartes_id_tecnica_i_ed7bba2a_uniq" UNIQUE ("bellasartes_id", "tecnica_id");
CREATE INDEX "Fondos_bellasartes_tecnica_bellasartes_id_64a13e1e" ON "Fondos_bellasartes_tecnica" ("bellasartes_id");
CREATE INDEX "Fondos_bellasartes_tecnica_tecnica_id_5ee71d3e" ON "Fondos_bellasartes_tecnica" ("tecnica_id");
