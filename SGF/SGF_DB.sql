-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Tempo de geração: 16/01/2019 às 14:43
-- Versão do servidor: 5.7.24-0ubuntu0.18.04.1
-- Versão do PHP: 7.2.10-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sgf`
create database sgf;
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `barracas`
--

CREATE TABLE `barracas` (
  `idBarraca` int(11) NOT NULL,
  `identificacao` varchar(20) DEFAULT NULL,
  `descricao` varchar(150) DEFAULT NULL,
  `tamanho` varchar(20) DEFAULT NULL,
  `localizacao` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `barracas`
--

INSERT INTO `barracas` (`idBarraca`, `identificacao`, `descricao`, `tamanho`, `localizacao`) VALUES
(3, 'A1', 'Com tenda', '3.00mx2.50m', 'Fila: A, N°: 1 '),
(4, 'A2', 'Sem tenda', '3.00mx2.50m', 'Fila: A, N°: 2');

-- --------------------------------------------------------

--
-- Estrutura para tabela `frequencia`
--

CREATE TABLE `frequencia` (
  `idFrequencia` int(11) NOT NULL,
  `idUsuario` int(11) DEFAULT NULL,
  `dataHora` varchar(25) DEFAULT NULL,
  `dataHoraMod` varchar(25) DEFAULT NULL,
  `idUsuarioMod` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `frequencia`
--

INSERT INTO `frequencia` (`idFrequencia`, `idUsuario`, `dataHora`, `dataHoraMod`, `idUsuarioMod`) VALUES
(1, 1, '15/01/2019 18:24', '15/01/2019 18:27', 1),
(2, 1, '15/01/2019 18:30', '15/01/2019 18:32', 2),
(3, 2, '15/01/2019 19:39', '15/01/2019 19:41', 1),
(4, 2, '16/01/2019 08:07', '16/01/2019 08:08', 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `lista_frequencia`
--

CREATE TABLE `lista_frequencia` (
  `idLista` int(11) NOT NULL,
  `idSocio` int(11) DEFAULT NULL,
  `status` varchar(8) DEFAULT NULL,
  `idFrequencia` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `lista_frequencia`
--

INSERT INTO `lista_frequencia` (`idLista`, `idSocio`, `status`, `idFrequencia`) VALUES
(1, 2, 'Presente', 1),
(2, 4, 'Presente', 1),
(3, 5, 'Ausente', 1),
(4, 2, 'Ausente', 2),
(5, 4, 'Presente', 2),
(6, 5, 'Presente', 2),
(7, 2, 'Presente', 3),
(8, 4, 'Presente', 3),
(9, 5, 'Presente', 3),
(10, 2, 'Presente', 4),
(11, 4, 'Presente', 4),
(12, 5, 'Presente', 4);

-- --------------------------------------------------------

--
-- Estrutura para tabela `reservas`
--

CREATE TABLE `reservas` (
  `idReserva` int(11) NOT NULL,
  `idUsuario` int(11) DEFAULT NULL,
  `idSocio` int(11) DEFAULT NULL,
  `idBarraca` int(11) DEFAULT NULL,
  `dataHora` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `reservas`
--

INSERT INTO `reservas` (`idReserva`, `idUsuario`, `idSocio`, `idBarraca`, `dataHora`) VALUES
(1, 1, 2, 4, '2019/01/03 13:45:48'),
(2, 2, 4, 3, '2019/01/03 13:46:15'),
(3, 1, 4, 3, '2019/01/05 17:06:04'),
(4, 1, 5, 4, '2019/01/15 19:46:44');

-- --------------------------------------------------------

--
-- Estrutura para tabela `socios`
--

CREATE TABLE `socios` (
  `idSocio` int(11) NOT NULL,
  `nome` varchar(150) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `endereco` varchar(150) DEFAULT NULL,
  `complemento` varchar(150) DEFAULT NULL,
  `dataCadastro` date DEFAULT NULL,
  `sexo` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `socios`
--

INSERT INTO `socios` (`idSocio`, `nome`, `cpf`, `telefone`, `endereco`, `complemento`, `dataCadastro`, `sexo`) VALUES
(2, 'José Oliveira', '16249593221', '(99) 99947-1234', 'Brejo do Amparo', 'Brejo do Amparo', '2018-12-21', 'M'),
(4, 'Ana Machado', '11111111111', '(99) 99999-0000', 'Brejo do Amparo', 'Brejo do Amparo', '2018-12-22', 'F'),
(5, 'Ilda Aparecida', '22222222222', '(99) 99999-0000', 'Gameleira, Gameleira', 'Próximo a Miguel do Leite', '2019-01-07', 'F');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `nome` varchar(150) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `endereco` varchar(150) DEFAULT NULL,
  `senha` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Fazendo dump de dados para tabela `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `nome`, `telefone`, `email`, `endereco`, `senha`) VALUES
(1, 'Admin', '(38) 99900-0016', 'agrijan@januaria.com.br', 'Rua 17, 150, Eldorado', '123456'),
(2, 'Joana', '(99) 99999-0000', 'joana@gomes.com', 'Rua 15, 465, Levinópolis', '12345');

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `barracas`
--
ALTER TABLE `barracas`
  ADD PRIMARY KEY (`idBarraca`);

--
-- Índices de tabela `frequencia`
--
ALTER TABLE `frequencia`
  ADD PRIMARY KEY (`idFrequencia`);

--
-- Índices de tabela `lista_frequencia`
--
ALTER TABLE `lista_frequencia`
  ADD PRIMARY KEY (`idLista`),
  ADD KEY `idFrequencia` (`idFrequencia`);

--
-- Índices de tabela `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`idReserva`);

--
-- Índices de tabela `socios`
--
ALTER TABLE `socios`
  ADD PRIMARY KEY (`idSocio`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `barracas`
--
ALTER TABLE `barracas`
  MODIFY `idBarraca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de tabela `frequencia`
--
ALTER TABLE `frequencia`
  MODIFY `idFrequencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de tabela `lista_frequencia`
--
ALTER TABLE `lista_frequencia`
  MODIFY `idLista` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT de tabela `reservas`
--
ALTER TABLE `reservas`
  MODIFY `idReserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT de tabela `socios`
--
ALTER TABLE `socios`
  MODIFY `idSocio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `lista_frequencia`
--
ALTER TABLE `lista_frequencia`
  ADD CONSTRAINT `lista_frequencia_ibfk_1` FOREIGN KEY (`idFrequencia`) REFERENCES `frequencia` (`idFrequencia`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
