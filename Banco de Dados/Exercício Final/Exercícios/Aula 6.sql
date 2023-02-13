CREATE TABLE alunos(
	Nro_Matricula INT GENERATED ALWAYS AS IDENTITY,
	nome VARCHAR(255) NOT NULL,
	cpf CHAR(11) NOT NULL UNIQUE,
	endereco VARCHAR(255),
	telefone INT,
	ano_Nasc DATE,
	
	PRIMARY KEY (Nro_Matricula)
	
);
INSERT INTO alunos
	VALUES ('DEFAULT', 'Abelardo', '12345678901', 'Rua bem ali', '85985858585', '10-08-1995');


CREATE TABLE disciplina(
	Cod_Disciplina INT GENERATED ALWAYS AS IDENTITY,
	nome VARCHAR(255) NOT NULL,
	cod_curso INT REFERENCES curso (id),

	PRIMARY KEY (Cod_Disciplina)
);
INSERT INTO disciplina 
	VALUES ('DEFAULT', 'HTML', '1');


CREATE TABLE matricula(
	Nro_matricula INT GENERATED ALWAYS AS IDENTITY,
	semestre INT,
	ano INT,
	Nro_faltas INT,
	
	PRIMARY KEY (Nro_matricula)
);
INSERT INTO matricula
	VALUES ('DEFAULT', '2', '2022', '5');