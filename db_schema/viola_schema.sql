--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: carrera_pc_componentes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.carrera_pc_componentes (
    id_carrera integer,
    min_cpu text NOT NULL,
    rec_cpu text NOT NULL,
    min_ram text NOT NULL,
    rec_ram text NOT NULL,
    min_storage text NOT NULL,
    rec_storage text NOT NULL,
    min_graphic text,
    rec_graphic text,
    CONSTRAINT check_id_carrera_valid CHECK ((id_carrera > 0))
);


ALTER TABLE public.carrera_pc_componentes OWNER TO postgres;

--
-- Name: carrera_universitaria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.carrera_universitaria (
    id integer NOT NULL,
    nombre text NOT NULL,
    area text NOT NULL,
    duracion double precision DEFAULT 0 NOT NULL
);


ALTER TABLE public.carrera_universitaria OWNER TO postgres;

--
-- Name: carrera_universitaria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.carrera_universitaria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.carrera_universitaria_id_seq OWNER TO postgres;

--
-- Name: carrera_universitaria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.carrera_universitaria_id_seq OWNED BY public.carrera_universitaria.id;


--
-- Name: column_meaning_translator; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.column_meaning_translator (
    column_name text NOT NULL,
    meaning text NOT NULL,
    table_name text NOT NULL
);


ALTER TABLE public.column_meaning_translator OWNER TO postgres;

--
-- Name: synonyms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.synonyms (
    raw_string text NOT NULL,
    real_word text NOT NULL,
    table_name text,
    column_name text
);


ALTER TABLE public.synonyms OWNER TO postgres;

--
-- Name: carrera_universitaria id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrera_universitaria ALTER COLUMN id SET DEFAULT nextval('public.carrera_universitaria_id_seq'::regclass);


--
-- Name: carrera_universitaria carrera_universitaria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrera_universitaria
    ADD CONSTRAINT carrera_universitaria_pkey PRIMARY KEY (id);


--
-- Name: carrera_universitaria nombre_carrera_unico; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrera_universitaria
    ADD CONSTRAINT nombre_carrera_unico UNIQUE (nombre);


--
-- Name: column_meaning_translator nombre_columna_unico; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.column_meaning_translator
    ADD CONSTRAINT nombre_columna_unico UNIQUE (column_name, table_name);


--
-- Name: carrera_pc_componentes carrera_pc_componentes_id_carrera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.carrera_pc_componentes
    ADD CONSTRAINT carrera_pc_componentes_id_carrera_fkey FOREIGN KEY (id_carrera) REFERENCES public.carrera_universitaria(id);


--
-- PostgreSQL database dump complete
--

