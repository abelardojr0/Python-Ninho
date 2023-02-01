import psycopg2

def criarLivros(conexao, cursor):
  cursor.execute('''
                DROP TABLE IF EXISTS livros;
				
				CREATE TABLE livros(
                 "Livro_ID" INT GENERATED ALWAYS AS IDENTITY,
                 "Livro_nome" VARCHAR(255),
                 "Livro_paginas" INT,
                 "Livro_anoLançamento" DATE,
                 "Livro_autor" VARCHAR(255),
                 "Autor_ID" INT,
        CONSTRAINT fk_autor
            FOREIGN KEY("Autor_ID")
            REFERENCES "autor"("Autor_ID")
            ON DELETE NO ACTION 
            ON UPDATE NO ACTION,
                  
                PRIMARY KEY ("Livro_ID")
		);
                 ''')
  conexao.commit()

def criarAutor(conexao, cursor):
  cursor.execute('''
                 DROP TABLE IF EXISTS "autor";
                 
                 CREATE TABLE "autor"(
                   "Autor_ID" INT GENERATED ALWAYS AS IDENTITY,
                   "Autor_nome" VARCHAR(255),
                   
                   PRIMARY KEY("Autor_ID")
                 );
                 
                 ''')
  conexao.commit()


try:
  conexao = psycopg2.connect(database="Biblioteca", user="postgres", password="postgres", host="localhost", port="5432")
  
  cursor = conexao.cursor()
  print("Conectado ao banco")
  criarAutor(conexao, cursor)
  criarLivros(conexao, cursor)
  conexao.close()
  cursor.close()
except(Exception, psycopg2.Error) as error:
  print("Falha ao conectar com o banco", error)