-- Generado por Oracle SQL Developer Data Modeler 4.2.0.932
--   en:        2017-05-10 09:17:38 CEST
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



CREATE TABLE arqueo_materiales (
    arqueologia_idarque         INTEGER NOT NULL,
    materiales_idmat            INTEGER NOT NULL,
    arqueologia_objeto_numinv   INTEGER NOT NULL
);

ALTER TABLE arqueo_materiales ADD CONSTRAINT arqueo_materiales_pk PRIMARY KEY ( arqueologia_idarque,materiales_idmat,arqueologia_objeto_numinv
 );

CREATE TABLE arqueologia (
    idarque         INTEGER NOT NULL,
    nombre          VARCHAR2(20) NOT NULL,
    hallazgos       CLOB,
    depositadopor   VARCHAR2(20) NOT NULL,
    nivcon          INTEGER NOT NULL,
    edad            VARCHAR2(20),
    objeto_numinv   INTEGER NOT NULL,
    idarq           INTEGER NOT NULL
);

CREATE UNIQUE INDEX arqueologia__idx ON
    arqueologia ( objeto_numinv ASC );

ALTER TABLE arqueologia ADD CONSTRAINT arqueologia_pk PRIMARY KEY ( objeto_numinv );

CREATE TABLE autores (
    idaut                        INTEGER NOT NULL,
    nomaut                       VARCHAR2(20 CHAR),
    apeaut                       VARCHAR2(20 CHAR),
    fechanac                     VARCHAR2(20 CHAR),
    fechadef                     VARCHAR2(20 CHAR),
    alias                        VARCHAR2(30 CHAR),
    bellas_artes_idba            INTEGER NOT NULL,
    bellas_artes_adquirido       VARCHAR2(15) NOT NULL,
    bellas_artes_objeto_numinv   INTEGER NOT NULL
);

CREATE UNIQUE INDEX autores__idx ON
    autores (
        bellas_artes_idba
    ASC,
        bellas_artes_adquirido
    ASC );

CREATE UNIQUE INDEX autores__idx ON
    autores ( bellas_artes_objeto_numinv ASC );

ALTER TABLE autores ADD CONSTRAINT autores_pk PRIMARY KEY ( idaut );

CREATE TABLE ba_soportes (
    bellas_artes_idba            INTEGER NOT NULL,
    bellas_artes_adquirido       VARCHAR2(15) NOT NULL,
    soportes_idsop               INTEGER NOT NULL,
    bellas_artes_objeto_numinv   INTEGER
);

ALTER TABLE ba_soportes ADD CONSTRAINT ba_soportes_pk PRIMARY KEY ( bellas_artes_idba,bellas_artes_adquirido,soportes_idsop,bellas_artes_objeto_numinv
 );

CREATE TABLE bellas_artes (
    idba            INTEGER NOT NULL,
    titulo          VARCHAR2(30 CHAR),
    procedencia     VARCHAR2(20 CHAR),
    adquirido       VARCHAR2(15 CHAR) NOT NULL,
    objeto_numinv   INTEGER NOT NULL,
    idba2           INTEGER NOT NULL
);

CREATE UNIQUE INDEX bellas_artes__idx ON
    bellas_artes ( objeto_numinv ASC );

ALTER TABLE bellas_artes ADD CONSTRAINT bellas_artes_pk PRIMARY KEY ( objeto_numinv );

CREATE TABLE cultura (
    idcul                       INTEGER NOT NULL,
    nomcul                      VARCHAR2(20) NOT NULL,
    arqueologia_idarque         INTEGER NOT NULL,
    arqueologia_objeto_numinv   INTEGER NOT NULL
);

ALTER TABLE cultura ADD CONSTRAINT cultura_pk PRIMARY KEY ( idcul );

CREATE TABLE donantes (
    iddon                        INTEGER NOT NULL,
    nomdon                       VARCHAR2(20 CHAR) NOT NULL,
    apedon                       VARCHAR2(40 CHAR) NOT NULL,
    dni                          VARCHAR2(13 CHAR),
    bellas_artes_idba            INTEGER NOT NULL,
    bellas_artes_adquirido       VARCHAR2(15) NOT NULL,
    bellas_artes_objeto_numinv   INTEGER NOT NULL
);

CREATE UNIQUE INDEX donantes__idx ON
    donantes (
        bellas_artes_idba
    ASC,
        bellas_artes_adquirido
    ASC );

CREATE UNIQUE INDEX donantes__idx ON
    donantes ( bellas_artes_objeto_numinv ASC );

ALTER TABLE donantes ADD CONSTRAINT donantes_pk PRIMARY KEY ( iddon );

CREATE TABLE estudios (
    idest                  INTEGER NOT NULL,
    nombre                 VARCHAR2 
--  ERROR: VARCHAR2 size not specified 
    ,
    informe_estado_idest   INTEGER NOT NULL
);

ALTER TABLE estudios ADD CONSTRAINT estudios_pk PRIMARY KEY ( idest );

CREATE TABLE informe_estado (
    idest            INTEGER NOT NULL,
    objet            CLOB,
    foto             BLOB,
    informes_idinf   INTEGER NOT NULL
);

CREATE UNIQUE INDEX informe_estado__idx ON
    informe_estado ( informes_idinf ASC );

ALTER TABLE informe_estado ADD CONSTRAINT informe_estado_pk PRIMARY KEY ( idest );

CREATE TABLE informe_inter (
    idinter          INTEGER NOT NULL,
    descripcion      CLOB,
    informes_idinf   INTEGER NOT NULL,
    idinf            INTEGER NOT NULL
);

CREATE UNIQUE INDEX informe_inter__idx ON
    informe_inter ( informes_idinf ASC );

ALTER TABLE informe_inter ADD CONSTRAINT informe_inter_pk PRIMARY KEY ( idinter );

CREATE TABLE informes (
    idinf        INTEGER NOT NULL,
    fechainf     DATE,
    prioridad    INTEGER,
    conclusion   CLOB,
    ape_rest     VARCHAR2(20) NOT NULL,
    nom_rest     VARCHAR2(30)
);

ALTER TABLE informes ADD CONSTRAINT informes_pk PRIMARY KEY ( idinf );

CREATE TABLE localidades (
    idloc               INTEGER NOT NULL,
    nomloc              VARCHAR2(20 CHAR) NOT NULL,
    yacimientos_idyac   INTEGER NOT NULL
);

ALTER TABLE localidades ADD CONSTRAINT localidades_pk PRIMARY KEY ( idloc );

CREATE TABLE materiales (
    idmat    INTEGER NOT NULL,
    nommat   VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE materiales ADD CONSTRAINT materiales_pk PRIMARY KEY ( idmat );

CREATE TABLE movimientos (
    idmov         INTEGER NOT NULL,
    museo         VARCHAR2 
--  ERROR: VARCHAR2 size not specified 
     NOT NULL,
    fechavuelta   DATE NOT NULL,
    fechaida      DATE NOT NULL,
    nomexpo       VARCHAR2(30) NOT NULL
);

ALTER TABLE movimientos ADD CONSTRAINT movimientos_pk PRIMARY KEY ( idmov );

CREATE TABLE objeto (
    numinv         INTEGER NOT NULL,
    dimensiones    VARCHAR2(10 CHAR),
    propietario    VARCHAR2(2 CHAR),
    datacion       VARCHAR2(20 CHAR) NOT NULL,
    fechaingreso   VARCHAR2 
--  ERROR: VARCHAR2 size not specified 
    ,
    descripcion    CLOB
);

ALTER TABLE objeto ADD CONSTRAINT objeto_pk PRIMARY KEY ( numinv );

CREATE TABLE objeto_informes (
    informes_idinf   INTEGER NOT NULL,
    objeto_numinv    INTEGER NOT NULL
);

ALTER TABLE objeto_informes ADD CONSTRAINT objeto_informes_pk PRIMARY KEY ( informes_idinf,objeto_numinv );

CREATE TABLE objeto_movimientos (
    objeto_numinv       INTEGER NOT NULL,
    movimientos_idmov   INTEGER NOT NULL
);

ALTER TABLE objeto_movimientos ADD CONSTRAINT objeto_movimientos_pk PRIMARY KEY ( objeto_numinv,movimientos_idmov );

CREATE TABLE ref_bibliografica (
    idbib       INTEGER NOT NULL,
    nombreaut   VARCHAR2(20),
    apeaut      VARCHAR2(20),
    año         INTEGER,
    isbn        VARCHAR2(13 CHAR),
    url         httpuritype
);

ALTER TABLE ref_bibliografica ADD CONSTRAINT ref_bibliografica_pk PRIMARY KEY ( idbib );

CREATE TABLE relation_2 (
    numinv_idbib   INTEGER NOT NULL,
    idbib          INTEGER NOT NULL
);

ALTER TABLE relation_2 ADD CONSTRAINT objeto_bibliografia PRIMARY KEY ( numinv_idbib,idbib );

CREATE TABLE secciones (
    idsec                       INTEGER NOT NULL,
    nomsec                      VARCHAR2(15) NOT NULL,
    arqueologia_idarque         INTEGER NOT NULL,
    arqueologia_objeto_numinv   INTEGER NOT NULL
);

ALTER TABLE secciones ADD CONSTRAINT secciones_pk PRIMARY KEY ( idsec );

CREATE TABLE series (
    idser                       INTEGER NOT NULL,
    nomser                      VARCHAR2(20 CHAR) NOT NULL,
    arqueologia_idarque         INTEGER NOT NULL,
    arqueologia_objeto_numinv   INTEGER NOT NULL
);

ALTER TABLE series ADD CONSTRAINT series_pk PRIMARY KEY ( idser );

CREATE TABLE soportes (
    idsop    INTEGER NOT NULL,
    nomsop   VARCHAR2(20 CHAR) NOT NULL
);

ALTER TABLE soportes ADD CONSTRAINT soportes_pk PRIMARY KEY ( idsop );

CREATE TABLE ubicación (
    idubi           INTEGER NOT NULL,
    exposicion      CHAR(1) NOT NULL,
    nombreubi       VARCHAR2 
--  ERROR: VARCHAR2 size not specified 
    ,
    objeto_numinv   INTEGER NOT NULL
);

CREATE UNIQUE INDEX ubicación__idx ON
    ubicación ( objeto_numinv ASC );

ALTER TABLE ubicación ADD CONSTRAINT ubicación_pk PRIMARY KEY ( idubi );

CREATE TABLE yacimientos (
    idyac                       INTEGER NOT NULL,
    nomyac                      VARCHAR2(30 CHAR),
    arqueologia_idarque         INTEGER NOT NULL,
    arqueologia_objeto_numinv   INTEGER NOT NULL
);

ALTER TABLE yacimientos ADD CONSTRAINT yacimientos_pk PRIMARY KEY ( idyac );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE arqueo_materiales ADD CONSTRAINT arqueo_materiales_arqueologia_fk FOREIGN KEY ( arqueologia_idarque )
    REFERENCES arqueologia ( objeto_numinv );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE arqueo_materiales ADD CONSTRAINT arqueo_materiales_arqueologia_fkv1 FOREIGN KEY ( arqueologia_objeto_numinv )
    REFERENCES arqueologia ( objeto_numinv );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE arqueo_materiales ADD CONSTRAINT arqueo_materiales_materiales_fk FOREIGN KEY ( materiales_idmat )
    REFERENCES materiales ( idmat );

ALTER TABLE arqueologia ADD CONSTRAINT arqueologia_objeto_fk FOREIGN KEY ( objeto_numinv )
    REFERENCES objeto ( numinv );

ALTER TABLE autores ADD CONSTRAINT autores_bellas_artes_fk FOREIGN KEY ( bellas_artes_objeto_numinv )
    REFERENCES bellas_artes ( objeto_numinv );

ALTER TABLE ba_soportes ADD CONSTRAINT ba_soportes_bellas_artes_fk FOREIGN KEY ( bellas_artes_objeto_numinv,bellas_artes_idba,bellas_artes_adquirido
 )
    REFERENCES bellas_artes ( objeto_numinv );

ALTER TABLE ba_soportes ADD CONSTRAINT ba_soportes_soportes_fk FOREIGN KEY ( soportes_idsop )
    REFERENCES soportes ( idsop );

ALTER TABLE bellas_artes ADD CONSTRAINT bellas_artes_objeto_fk FOREIGN KEY ( objeto_numinv )
    REFERENCES objeto ( numinv );

ALTER TABLE relation_2 ADD CONSTRAINT bibliografia_fk FOREIGN KEY ( idbib )
    REFERENCES ref_bibliografica ( idbib );

ALTER TABLE cultura ADD CONSTRAINT cultura_arqueologia_fk FOREIGN KEY ( arqueologia_objeto_numinv )
    REFERENCES arqueologia ( objeto_numinv );

ALTER TABLE donantes ADD CONSTRAINT donantes_bellas_artes_fk FOREIGN KEY ( bellas_artes_objeto_numinv )
    REFERENCES bellas_artes ( objeto_numinv );

ALTER TABLE estudios ADD CONSTRAINT estudios_informe_estado_fk FOREIGN KEY ( informe_estado_idest )
    REFERENCES informe_estado ( idest );

ALTER TABLE informe_estado ADD CONSTRAINT informe_estado_informes_fk FOREIGN KEY ( informes_idinf )
    REFERENCES informes ( idinf );

ALTER TABLE informe_inter ADD CONSTRAINT informe_inter_informes_fk FOREIGN KEY ( informes_idinf )
    REFERENCES informes ( idinf );

ALTER TABLE localidades ADD CONSTRAINT localidades_yacimientos_fk FOREIGN KEY ( yacimientos_idyac )
    REFERENCES yacimientos ( idyac );

ALTER TABLE relation_2 ADD CONSTRAINT objeto_fk FOREIGN KEY ( numinv_idbib )
    REFERENCES objeto ( numinv );

ALTER TABLE objeto_informes ADD CONSTRAINT objeto_informes_informes_fk FOREIGN KEY ( informes_idinf )
    REFERENCES informes ( idinf );

ALTER TABLE objeto_informes ADD CONSTRAINT objeto_informes_objeto_fk FOREIGN KEY ( objeto_numinv )
    REFERENCES objeto ( numinv );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE objeto_movimientos ADD CONSTRAINT objeto_movimientos_movimientos_fk FOREIGN KEY ( movimientos_idmov )
    REFERENCES movimientos ( idmov );

ALTER TABLE objeto_movimientos ADD CONSTRAINT objeto_movimientos_objeto_fk FOREIGN KEY ( objeto_numinv )
    REFERENCES objeto ( numinv );

ALTER TABLE secciones ADD CONSTRAINT secciones_arqueologia_fk FOREIGN KEY ( arqueologia_objeto_numinv )
    REFERENCES arqueologia ( objeto_numinv );

ALTER TABLE series ADD CONSTRAINT series_arqueologia_fk FOREIGN KEY ( arqueologia_objeto_numinv )
    REFERENCES arqueologia ( objeto_numinv );

ALTER TABLE ubicación ADD CONSTRAINT ubicación_objeto_fk FOREIGN KEY ( objeto_numinv )
    REFERENCES objeto ( numinv );

ALTER TABLE yacimientos ADD CONSTRAINT yacimientos_arqueologia_fk FOREIGN KEY ( arqueologia_objeto_numinv )
    REFERENCES arqueologia ( objeto_numinv );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            24
-- CREATE INDEX                             9
-- ALTER TABLE                             48
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   8
-- WARNINGS                                 0
