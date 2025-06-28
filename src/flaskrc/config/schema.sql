PRAGMA foreign_keys = ON;

-- Tabela: Usuario
CREATE TABLE IF NOT EXISTS Usuario (
  id_usr INTEGER PRIMARY KEY NOT NULL,
  nm_usr TEXT NOT NULL,
  dt_cad DATE NOT NULL,
  ic_atv CHAR(1) NOT NULL
);

-- Tabela: Produto
CREATE TABLE IF NOT EXISTS Produto (
  id_prd INTEGER PRIMARY KEY NOT NULL,
  nm_prd TEXT NOT NULL,
  ds_prd TEXT NOT NULL,
  ic_atv CHAR(1) NOT NULL,
  qtd_est_min INTEGER NOT NULL,
  id_usr INTEGER NOT NULL,
  dt_cad DATE NOT NULL,
  FOREIGN KEY (id_usr) REFERENCES Usuario(id_usr)
);

-- Tabela: TipoMovimentacao
CREATE TABLE IF NOT EXISTS TipoMovimentacao (
  id_tp_mov INTEGER PRIMARY KEY NOT NULL,
  nm_tp_mov TEXT NOT NULL,
  ds_tp_mov TEXT NOT NULL,
  ic_mov CHAR(1) NOT NULL,
  dt_cad DATE NOT NULL
);

-- Tabela: Movimentacao
CREATE TABLE IF NOT EXISTS Movimentacao (
  id_mov INTEGER PRIMARY KEY NOT NULL,
  id_prd INTEGER NOT NULL,
  id_tp_mov INTEGER NOT NULL,
  qtd_mov INTEGER NOT NULL,
  dt_mov DATE NOT NULL,
  dt_cad DATE NOT NULL,
  id_usr INTEGER NOT NULL,
  FOREIGN KEY (id_usr) REFERENCES Usuario(id_usr),
  FOREIGN KEY (id_prd) REFERENCES Produto(id_prd),
  FOREIGN KEY (id_tp_mov) REFERENCES TipoMovimentacao(id_tp_mov)
);

-- Tabela: GrupoAcesso
CREATE TABLE IF NOT EXISTS GrupoAcesso (
  id_grp_acs INTEGER PRIMARY KEY NOT NULL,
  nm_grp_acs TEXT NOT NULL,
  ds_grp_acs TEXT NOT NULL,
  ic_atv CHAR(1) NOT NULL,
  dt_cad DATE NOT NULL
);

-- Tabela: UsuarioAcessoDetalhe
CREATE TABLE IF NOT EXISTS UsuarioAcessoDetalhe (
  id_usr_dtl INTEGER PRIMARY KEY NOT NULL,
  id_usr INTEGER NOT NULL,
  id_grp_acs INTEGER NOT NULL,
  FOREIGN KEY (id_usr) REFERENCES Usuario(id_usr),
  FOREIGN KEY (id_grp_acs) REFERENCES GrupoAcesso(id_grp_acs)
);
