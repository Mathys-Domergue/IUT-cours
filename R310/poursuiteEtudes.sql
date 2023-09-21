-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 11, 2022 at 06:44 PM
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
-- Table structure for table `poursuiteEtudes`
--

CREATE TABLE `poursuiteEtudes` (
  `id` int(10) UNSIGNED NOT NULL,
  `lyceen` int(10) DEFAULT NULL,
  `ecole` varchar(100) COLLATE latin1_general_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `poursuiteEtudes`
--

INSERT INTO `poursuiteEtudes` (`id`, `lyceen`, `ecole`) VALUES
(1, 216, 'Prépa MPSI - Montpellier'),
(2, 90, 'Dept. Info - IUT de Montpellier'),
(3, 126, 'Dept. MMI - IUT de Béziers'),
(4, 36, NULL),
(5, 189, 'BTS SIO - Lycée J. MERMOZ - Montpellier'),
(6, 54, 'Dept. R&T - IUT de Valence'),
(7, 171, 'Prépa MPSI - Montpellier'),
(8, 72, 'Dept. Info - IUT de Montpellier'),
(9, 63, 'BTS SIO - Lycée J. MERMOZ - Montpellier'),
(10, 207, 'BTS Électrotechnique - Lycée J. MOULIN - Béziers'),
(11, 198, 'Dept. R&T - IUT de Valence'),
(12, 117, 'Dept. R&T - IUT de Béziers'),
(13, 153, 'Prépa MPSI - Montpellier'),
(14, 180, 'Dept. Info - IUT de Montpellier'),
(15, 99, 'BTS Électrotechnique - Lycée J. MOULIN - Béziers'),
(16, 234, 'Dept. R&T - IUT de Valence'),
(17, 162, 'BTS SIO - Lycée J. MERMOZ - Montpellier'),
(18, 225, 'BTS SIO - Lycée J. MERMOZ - Montpellier'),
(19, 9, 'Prépa MPSI - Montpellier'),
(20, 18, 'BTS Électrotechnique - Lycée J. MOULIN - Béziers'),
(21, 108, 'BTS SIO - Lycée J. MERMOZ - Montpellier'),
(22, 27, 'Dept. R&T - IUT de Béziers'),
(23, 45, 'Dept. Info - IUT de Montpellier'),
(24, 144, 'Dept. MMI - IUT de Béziers'),
(25, 81, 'Prépa MPSI - Montpellier'),
(26, 135, 'Dept. R&T - IUT de Valence'),
(27, 243, 'Dept. R&T - IUT de Béziers'),
(28, 45, NULL),
(29, 90, 'BTS SIO - Lycée J. MERMOZ - Montpellier'),
(30, 135, NULL),
(31, 180, 'Prépa MPSI - Montpellier'),
(32, 225, 'Prépa MPSI - Montpellier');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `poursuiteEtudes`
--
ALTER TABLE `poursuiteEtudes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `poursuiteEtudes`
--
ALTER TABLE `poursuiteEtudes`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
