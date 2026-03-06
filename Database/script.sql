CREATE TABLE cargos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    ascensao BOOLEAN DEFAULT FALSE
);


CREATE TABLE salarios (
    id_cargo INT NOT NULL REFERENCES cargos(id) ON DELETE CASCADE,
    salario_junior DOUBLE PRECISION,
    salario_pleno DOUBLE PRECISION,
    salario_senior DOUBLE PRECISION,
    ano INT,
    PRIMARY KEY (id_cargo, ano)
);


ALTER TABLE salarios
ADD COLUMN media DOUBLE PRECISION;

INSERT INTO cargos (id, nome, ascensao)
VALUES 
(1, 'Administrador de Banco de Dados', false),
(2, 'Administrador de Rede', false);

DROP table cargos;

CREATE TABLE empresas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    linkedin VARCHAR(255),
    imagem VARCHAR(255)
)