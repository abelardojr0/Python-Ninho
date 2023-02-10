# CREATE TABLE jogos(
# 	id INT GENERATED ALWAYS AS IDENTITY,
# 	nome VARCHAR(255) NOT NULL,
# 	duracao INT,
# 	numJogadores VARCHAR(255),
# 	idade INT,
# 	editora VARCHAR(255),
	
# 	PRIMARY KEY (id)
	
# );

# CREATE TABLE usuarios(
# 	id INT GENERATED ALWAYS AS IDENTITY,
# 	nome VARCHAR(255) NOT NULL,
# 	cpf CHAR(11),
# 	anoNasc DATE,
# 	login VARCHAR(255) NOT NULL,
# 	senha VARCHAR(255) NOT NULL,
	
# 	PRIMARY KEY (id)
	
# );

# CREATE TABLE colecao(
# 	id INT GENERATED ALWAYS AS IDENTITY,
# 	id_usuario INT NOT NULL,
	
# 	CONSTRAINT fk_usuario
# 		FOREIGN KEY (id_usuario)
# 			REFERENCES usuarios (id)
# 			ON DELETE NO ACTION
# 			ON UPDATE NO ACTION,
	
# 	PRIMARY KEY (id)
	
# );

# CREATE TABLE colecao_jogos(
# 	id INT GENERATED ALWAYS AS IDENTITY,
# 	id_colecao INT NOT NULL,
# 	id_jogo INT NOT NULL,
	
# 	CONSTRAINT fk_colecao
# 		FOREIGN KEY (id_colecao)
# 			REFERENCES colecao (id)
# 			ON DELETE NO ACTION
# 			ON UPDATE NO ACTION,
	
# 	CONSTRAINT fk_jogo
# 		FOREIGN KEY (id_jogo)
# 			REFERENCES jogos (id)
# 			ON DELETE NO ACTION
# 			ON UPDATE NO ACTION,
	
# 	PRIMARY KEY(id)
# );

# INSERT INTO jogos 
# 	VALUES
# 		(DEFAULT, 'Arcadia Quest', '120', '1-4', '12', 'Galapagos'),
# 		(DEFAULT, 'Coup', '10', '4-10', '10', 'Mandala');
		
# INSERT INTO usuarios 
# 	VALUES
# 		(DEFAULT, 'Abelardo Júnior', '12345678901', '10-08-1995', 'abel', '123'),
# 		(DEFAULT, 'Andressa Alencar', '12345678902', '08-08-1990' , 'anndy', '456');
		
# SELECT * FROM jogos