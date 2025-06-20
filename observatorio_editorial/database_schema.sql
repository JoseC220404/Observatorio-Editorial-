--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-04-06 00:20:38

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 260 (class 1255 OID 17626)
-- Name: auditoria_fuente(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.auditoria_fuente() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_nuevos)
        VALUES ('fuente', 'INSERT', current_user, to_jsonb(NEW));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos, datos_nuevos)
        VALUES ('fuente', 'UPDATE', current_user, to_jsonb(OLD), to_jsonb(NEW));
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos)
        VALUES ('fuente', 'DELETE', current_user, to_jsonb(OLD));
    END IF;
    RETURN NULL;  -- No es necesario devolver un valor en un trigger AFTER
END;
$$;


ALTER FUNCTION public.auditoria_fuente() OWNER TO postgres;

--
-- TOC entry 262 (class 1255 OID 17628)
-- Name: auditoria_organizacion(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.auditoria_organizacion() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_nuevos)
        VALUES ('organizacion', 'INSERT', current_user, to_jsonb(NEW));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos, datos_nuevos)
        VALUES ('organizacion', 'UPDATE', current_user, to_jsonb(OLD), to_jsonb(NEW));
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos)
        VALUES ('organizacion', 'DELETE', current_user, to_jsonb(OLD));
    END IF;
    RETURN NULL;
END;
$$;


ALTER FUNCTION public.auditoria_organizacion() OWNER TO postgres;

--
-- TOC entry 261 (class 1255 OID 17627)
-- Name: auditoria_persona(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.auditoria_persona() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_nuevos)
        VALUES ('persona', 'INSERT', current_user, to_jsonb(NEW));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos, datos_nuevos)
        VALUES ('persona', 'UPDATE', current_user, to_jsonb(OLD), to_jsonb(NEW));
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO auditoria (tabla_afectada, operacion, usuario, datos_antiguos)
        VALUES ('persona', 'DELETE', current_user, to_jsonb(OLD));
    END IF;
    RETURN NULL;
END;
$$;


ALTER FUNCTION public.auditoria_persona() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 247 (class 1259 OID 17663)
-- Name: Campo_de_conocimiento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Campo_de_conocimiento" (
    campo_id integer NOT NULL,
    nombre_del_campo character varying(100) NOT NULL
);


ALTER TABLE public."Campo_de_conocimiento" OWNER TO postgres;

--
-- TOC entry 246 (class 1259 OID 17647)
-- Name: Categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Categoria" (
    id_categoria integer NOT NULL,
    nombre character varying(250) NOT NULL
);


ALTER TABLE public."Categoria" OWNER TO postgres;

--
-- TOC entry 245 (class 1259 OID 17646)
-- Name: Categoria_id_categoria_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Categoria_id_categoria_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Categoria_id_categoria_seq" OWNER TO postgres;

--
-- TOC entry 5224 (class 0 OID 0)
-- Dependencies: 245
-- Name: Categoria_id_categoria_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Categoria_id_categoria_seq" OWNED BY public."Categoria".id_categoria;


--
-- TOC entry 251 (class 1259 OID 17918)
-- Name: Cobertura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cobertura" (
    id_cobertura integer NOT NULL,
    cobertura character varying(250) NOT NULL
);


ALTER TABLE public."Cobertura" OWNER TO postgres;

--
-- TOC entry 248 (class 1259 OID 17719)
-- Name: Codigo_Postal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Codigo_Postal" (
    id_codigo character varying(250) NOT NULL
);


ALTER TABLE public."Codigo_Postal" OWNER TO postgres;

--
-- TOC entry 254 (class 1259 OID 17933)
-- Name: Condicion_de_la_licencia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Condicion_de_la_licencia" (
    id_condicion_de_la_licencia integer NOT NULL,
    condicion_de_la_licencia character varying(250) NOT NULL
);


ALTER TABLE public."Condicion_de_la_licencia" OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16466)
-- Name: Corresponde_A; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Corresponde_A" (
    materias__idem character varying(25) NOT NULL,
    ejetem__ideje character varying(25) NOT NULL
);


ALTER TABLE public."Corresponde_A" OWNER TO postgres;

-- Tabla de auditoria (mencionada en las funciones de trigger)
CREATE TABLE IF NOT EXISTS public.auditoria (
    id_auditoria SERIAL PRIMARY KEY,
    tabla_afectada VARCHAR(100) NOT NULL,
    operacion VARCHAR(10) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    datos_antiguos JSONB,
    datos_nuevos JSONB
);