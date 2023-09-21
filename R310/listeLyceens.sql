-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 11, 2022 at 06:40 PM
-- Server version: 10.6.8-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `GdL`
--

-- --------------------------------------------------------

--
-- Table structure for table `listeLyceens`
--

CREATE TABLE `listeLyceens` (
  `id` int(10) UNSIGNED NOT NULL,
  `nom` varchar(50) COLLATE latin1_general_ci DEFAULT NULL,
  `prenom` varchar(50) COLLATE latin1_general_ci DEFAULT NULL,
  `classe` varchar(10) COLLATE latin1_general_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `listeLyceens`
--

INSERT INTO `listeLyceens` (`id`, `nom`, `prenom`, `classe`) VALUES
(1, 'MARTIN', 'Yoann', 'TC2'),
(2, 'BERNARD', 'Abélard', 'TC3'),
(3, 'THOMAS', 'Séverin', 'TC4'),
(4, 'PETIT', 'Althée', 'TC5'),
(5, 'ROBERT', 'Kevin', 'TG1'),
(6, 'RICHARD', 'Abeline', 'TG2'),
(7, 'DURAND', 'Alaine', 'TG3'),
(8, 'DUBOIS', 'Camillien', 'TS1'),
(9, 'MOREAU', 'Pierre', 'TC1'),
(10, 'LAURENT', 'Yankel', 'TC2'),
(11, 'SIMON', 'Malo', 'TC3'),
(12, 'MICHEL', 'Gerberge', 'TC4'),
(13, 'LEFEBVRE', 'Éloi', 'TC5'),
(14, 'LEROY', 'Sylvain', 'TG1'),
(15, 'ROUX', 'Quentin', 'TG2'),
(16, 'DAVID', 'Mathis', 'TG3'),
(17, 'BERTRAND', 'Gladys', 'TS1'),
(18, 'MOREL', 'Pascaline', 'TC1'),
(19, 'FOURNIER', 'Damien', 'TC2'),
(20, 'GIRARD', 'Séverin', 'TC3'),
(21, 'BONNET', 'Amiel', 'TC4'),
(22, 'DUPONT', 'Lionel', 'TC5'),
(23, 'LAMBERT', 'Ermengarde', 'TG1'),
(24, 'FONTAINE', 'Abigaïl', 'TG2'),
(25, 'ROUSSEAU', 'Ansbert', 'TG3'),
(26, 'VINCENT', 'Frédéric', 'TS1'),
(27, 'MULLER', 'Adalsinde', 'TC1'),
(28, 'LEFEVRE', 'Alcée', 'TC2'),
(29, 'FAURE', 'Loup', 'TC3'),
(30, 'ANDRE', 'Camille', 'TC4'),
(31, 'MERCIER', 'Adalbaude', 'TC5'),
(32, 'BLANC', 'Amandine', 'TG1'),
(33, 'GUERIN', 'Lennaic', 'TG2'),
(34, 'BOYER', 'Ambroisine', 'TG3'),
(35, 'GARNIER', 'Elsa', 'TS1'),
(36, 'CHEVALIER', 'Ameline', 'TC1'),
(37, 'FRANCOIS', 'Amantine', 'TC2'),
(38, 'LEGRAND', 'Soline ou solène\"', 'TC3'),
(39, 'GAUTHIER', 'Clémentine', 'TC4'),
(40, 'GARCIA', 'Amaryllis', 'TC5'),
(41, 'PERRIN', 'Agénor', 'TG1'),
(42, 'ROBIN', 'Hugues', 'TG2'),
(43, 'CLEMENT', 'Oscar', 'TG3'),
(44, 'MORIN', 'Aldric', 'TS1'),
(45, 'NICOLAS', 'Delphine', 'TC1'),
(46, 'HENRY', 'Aymard', 'TC2'),
(47, 'ROUSSEL', 'Lauren', 'TC3'),
(48, 'MATHIEU', 'Adegrin', 'TC4'),
(49, 'GAUTIER', 'Aurélien', 'TC5'),
(50, 'MASSON', 'Yoann', 'TG1'),
(51, 'MARCHAND', 'Adel', 'TG2'),
(52, 'DUVAL', 'Tancrède', 'TG3'),
(53, 'DENIS', 'Hortense', 'TS1'),
(54, 'DUMONT', 'Harmonie', 'TC1'),
(55, 'MARIE', 'Pécine', 'TC2'),
(56, 'LEMAIRE', 'Nadège', 'TC3'),
(57, 'NOEL', 'Clémentine', 'TC4'),
(58, 'MEYER', 'Anselme', 'TC5'),
(59, 'DUFOUR', 'Aliénor', 'TG1'),
(60, 'MEUNIER', 'Herbert', 'TG2'),
(61, 'BRUN', 'Karine', 'TG3'),
(62, 'BLANCHARD', 'Mence', 'TS1'),
(63, 'GIRAUD', 'Réjean', 'TC1'),
(64, 'JOLY', 'Clément', 'TC2'),
(65, 'RIVIERE', 'Claire', 'TC3'),
(66, 'LUCAS', 'Auriane', 'TC4'),
(67, 'BRUNET', 'Aimé', 'TC5'),
(68, 'GAILLARD', 'Angélique', 'TG1'),
(69, 'BARBIER', 'Harmonie', 'TG2'),
(70, 'ARNAUD', 'Odile', 'TG3'),
(71, 'MARTINEZ', 'Mauricet', 'TS1'),
(72, 'GERARD', 'Tanguy', 'TC1'),
(73, 'ROCHE', 'Athénaïs', 'TC2'),
(74, 'RENARD', 'Aubertine', 'TC3'),
(75, 'SCHMITT', 'Stanislas', 'TC4'),
(76, 'LEROUX', 'Igor', 'TC5'),
(77, 'COLIN', 'Clarence', 'TG1'),
(78, 'VIDAL', 'Ludovic', 'TG2'),
(79, 'CARON', 'Fiacre', 'TG3'),
(80, 'PICARD', 'Auriane', 'TS1'),
(81, 'ROGER', 'Achaire', 'TC1'),
(82, 'FABRE', 'Althée', 'TC2'),
(83, 'AUBERT', 'Hilaire', 'TC3'),
(84, 'LEMOINE', 'Valéry', 'TC4'),
(85, 'RENAUD', 'Alcée', 'TC5'),
(86, 'DUMAS', 'Eugénie', 'TG1'),
(87, 'LACROIX', 'Andoche', 'TG2'),
(88, 'OLIVIER', 'Gaston', 'TG3'),
(89, 'PHILIPPE', 'Innocent', 'TS1'),
(90, 'BOURGEOIS', 'Rébecca', 'TC1'),
(91, 'PIERRE', 'Anselme', 'TC2'),
(92, 'BENOIT', 'Amarande', 'TC3'),
(93, 'LECLERC', 'Jacqueline', 'TC4'),
(94, 'PAYET', 'Ancelin', 'TC5'),
(95, 'ROLLAND', 'Leufroy', 'TG1'),
(96, 'LECLERCQ', 'Lennaic', 'TG2'),
(97, 'GUILLAUME', 'Aloys', 'TG3'),
(98, 'LECOMTE', 'Diogène', 'TS1'),
(99, 'LOPEZ', 'Jourdain', 'TC1'),
(100, 'JEAN', 'Antigone', 'TC2'),
(101, 'DUPUY', 'Aignane', 'TC3'),
(102, 'GUILLOT', 'Louis', 'TC4'),
(103, 'HUBERT', 'Aldegonde', 'TC5'),
(104, 'BERGER', 'Leufroy', 'TG1'),
(105, 'CARPENTIER', 'Emma', 'TG2'),
(106, 'SANCHEZ', 'Thomas', 'TG3'),
(107, 'DUPUIS', 'Abel', 'TS1'),
(108, 'MOULIN', 'Amélien', 'TC1'),
(109, 'LOUIS', 'Caroline', 'TC2'),
(110, 'DESCHAMPS', 'Aloys', 'TC3'),
(111, 'HUET', 'Candide', 'TC4'),
(112, 'VASSEUR', 'Gilles', 'TC5'),
(113, 'PEREZ', 'Mamert', 'TG1'),
(114, 'BOUCHER', 'Aude', 'TG2'),
(115, 'FLEURY', 'Anthelmette', 'TG3'),
(116, 'ROYER', 'Yann', 'TS1'),
(117, 'KLEIN', 'Fulgence', 'TC1'),
(118, 'JACQUET', 'Claude', 'TC2'),
(119, 'ADAM', 'Fabien', 'TC3'),
(120, 'PARIS', 'Béatrix', 'TC4'),
(121, 'POIRIER', 'Primerose', 'TC5'),
(122, 'MARTY', 'Eugène', 'TG1'),
(123, 'AUBRY', 'Augustine', 'TG2'),
(124, 'GUYOT', 'Julien', 'TG3'),
(125, 'CARRE', 'Hector', 'TS1'),
(126, 'CHARLES', 'Gerberge', 'TC1'),
(127, 'RENAULT', 'Florentin', 'TC2'),
(128, 'CHARPENTIER', 'William', 'TC3'),
(129, 'MENARD', 'Pélagie', 'TC4'),
(130, 'MAILLARD', 'Hédelin', 'TC5'),
(131, 'BARON', 'Arminie', 'TG1'),
(132, 'BERTIN', 'Aristion', 'TG2'),
(133, 'BAILLY', 'Florence', 'TG3'),
(134, 'HERVE', 'Héloïse', 'TS1'),
(135, 'SCHNEIDER', 'Cyprien', 'TC1'),
(136, 'FERNANDEZ', 'Élisée', 'TC2'),
(137, 'LE GALL', 'Lionel', 'TC3'),
(138, 'COLLET', 'Gislebert', 'TC4'),
(139, 'LEGER', 'Alcée', 'TC5'),
(140, 'BOUVIER', 'Laura', 'TG1'),
(141, 'JULIEN', 'Bénédicte', 'TG2'),
(142, 'PREVOST', 'Ferdinand', 'TG3'),
(143, 'MILLET', 'Anthelmine', 'TS1'),
(144, 'PERROT', 'Réjean', 'TC1'),
(145, 'DANIEL', 'Delphine', 'TC2'),
(146, 'LE ROUX', 'Cosette', 'TC3'),
(147, 'COUSIN', 'Noël', 'TC4'),
(148, 'GERMAIN', 'Abeline', 'TC5'),
(149, 'BRETON', 'Adalbald', 'TG1'),
(150, 'BESSON', 'Avril', 'TG2'),
(151, 'LANGLOIS', 'Rébecca', 'TG3'),
(152, 'REMY', 'Aline', 'TS1'),
(153, 'LE GOFF', 'Agilberte', 'TC1'),
(154, 'PELLETIER', 'Aminte', 'TC2'),
(155, 'LEVEQUE', 'Célestin', 'TC3'),
(156, 'PERRIER', 'Annette', 'TC4'),
(157, 'LEBLANC', 'Gérard', 'TC5'),
(158, 'BARRE', 'Yannick', 'TG1'),
(159, 'LEBRUN', 'Cathaline', 'TG2'),
(160, 'MARCHAL', 'Armeline', 'TG3'),
(161, 'WEBER', 'Fulbert', 'TS1'),
(162, 'MALLET', 'Maximilien', 'TC1'),
(163, 'HAMON', 'Philothée', 'TC2'),
(164, 'BOULANGER', 'Asceline', 'TC3'),
(165, 'JACOB', 'Abélie', 'TC4'),
(166, 'MONNIER', 'Ève', 'TC5'),
(167, 'MICHAUD', 'Mireille', 'TG1'),
(168, 'RODRIGUEZ', 'Arnaude', 'TG2'),
(169, 'GUICHARD', 'Sylviane', 'TG3'),
(170, 'GILLET', 'Ariste', 'TS1'),
(171, 'ETIENNE', 'Andrée', 'TC1'),
(172, 'GRONDIN', 'Antide', 'TC2'),
(173, 'POULAIN', 'Aurore', 'TC3'),
(174, 'TESSIER', 'Théodore', 'TC4'),
(175, 'CHEVALLIER', 'Adrastée', 'TC5'),
(176, 'COLLIN', 'Amande', 'TG1'),
(177, 'CHAUVIN', 'Amiel', 'TG2'),
(178, 'DA SILVA', 'Gonthier', 'TG3'),
(179, 'BOUCHET', 'Céline', 'TS1'),
(180, 'LEMAITRE', 'Adélaïde', 'TC1'),
(181, 'BENARD', 'Elora', 'TC2'),
(182, 'MARECHAL', 'Aphélie', 'TC3'),
(183, 'HUMBERT', 'Anne', 'TC4'),
(184, 'REYNAUD', 'Serge', 'TC5'),
(185, 'ANTOINE', 'Aube', 'TG1'),
(186, 'HOARAU', 'Olive', 'TG2'),
(187, 'PERRET', 'Élie', 'TG3'),
(188, 'BARTHELEMY', 'Magali', 'TS1'),
(189, 'CORDIER', 'Florent', 'TC1'),
(190, 'PICHON', 'Cathaline', 'TC2'),
(191, 'LEJEUNE', 'Apollinaire', 'TC3'),
(192, 'GILBERT', 'Félix', 'TC4'),
(193, 'LAMY', 'Astérie', 'TC5'),
(194, 'DELAUNAY', 'Suzie', 'TG1'),
(195, 'PASQUIER', 'Corentine', 'TG2'),
(196, 'CARLIER', 'Augustine', 'TG3'),
(197, 'LAPORTE', 'Edith', 'TS1'),
(198, 'GROS', 'Clémentine', 'TC1'),
(199, 'BUISSON', 'Aline', 'TC2'),
(200, 'OLLIVIER', 'Adélice', 'TC3'),
(201, 'BRIAND', 'Amaliane', 'TC4'),
(202, 'ALEXANDRE', 'Sarah', 'TC5'),
(203, 'GEORGES', 'Astérie', 'TG1'),
(204, 'GUILLOU', 'Margaux', 'TG2'),
(205, 'BESNARD', 'Astride', 'TG3'),
(206, 'LEGROS', 'Baptiste', 'TS1'),
(207, 'GONZALEZ', 'Sarah', 'TC1'),
(208, 'COULON', 'Cléandre', 'TC2'),
(209, 'MAILLOT', 'Romain', 'TC3'),
(210, 'ALBERT', 'Margot', 'TC4'),
(211, 'CAMUS', 'Yoann', 'TC5'),
(212, 'DELATTRE', 'Agathon', 'TG1'),
(213, 'LAUNAY', 'Valéry', 'TG2'),
(214, 'HEBERT', 'Alizé', 'TG3'),
(215, 'LESAGE', 'Florence', 'TS1'),
(216, 'BLANCHET', 'Julien', 'TC1'),
(217, 'DIDIER', 'Emmanuel', 'TC2'),
(218, 'VOISIN', 'Douce', 'TC3'),
(219, 'PONS', 'Gaspard', 'TC4'),
(220, 'BOUSQUET', 'Armine', 'TC5'),
(221, 'COSTE', 'Estevan', 'TG1'),
(222, 'VALLEE', 'Morgane', 'TG2'),
(223, 'JACQUES', 'Agathon', 'TG3'),
(224, 'MARTEL', 'Norgot', 'TS1'),
(225, 'MAURY', 'Yseult', 'TC1'),
(226, 'RAYNAUD', 'Agneflète', 'TC2'),
(227, 'BARBE', 'Adalric', 'TC3'),
(228, 'PASCAL', 'Aymon', 'TC4'),
(229, 'BIGOT', 'Thibault', 'TC5'),
(230, 'VERDIER', 'Aymardine', 'TG1'),
(231, 'CHARRIER', 'Dimitri', 'TG2'),
(232, 'SAUVAGE', 'Odon\"', 'TG3'),
(233, 'GUILLET', 'Berthe', 'TS1'),
(234, 'MAHE', 'Fortuné', 'TC1'),
(235, 'LEDUC', 'Brice', 'TC2'),
(236, 'LELIEVRE', 'Ascelin', 'TC3'),
(237, 'GREGOIRE', 'Aricie', 'TC4'),
(238, 'JOUBERT', 'Manon', 'TC5'),
(239, 'MASSE', 'Malo', 'TG1'),
(240, 'DELMAS', 'Léa', 'TG2'),
(241, 'MORVAN', 'Gonzague', 'TG3'),
(242, 'LEBRETON', 'Ségolène', 'TS1'),
(243, 'TANGUY', 'Geoffroy', 'TC1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `listeLyceens`
--
ALTER TABLE `listeLyceens`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `listeLyceens`
--
ALTER TABLE `listeLyceens`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=992;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
