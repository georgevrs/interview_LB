-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 29, 2023 at 03:05 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `interview_lb`
--

-- --------------------------------------------------------

--
-- Table structure for table `companies`
--

CREATE TABLE `companies` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `gemh_number` varchar(50) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `registration_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `companies`
--

INSERT INTO `companies` (`id`, `name`, `gemh_number`, `website`, `registration_date`) VALUES
(16, 'ΠΑΝΑΓΙΩΣΘ΢ ΑΜΠΑΣΗΘ΢ ΚΑΙ ΢ΙΑ ΙΔΙΩΣΙΚΘ ΚΕΦΑΛΑΙΟΤΧΙΚΘ ΕΣΑΙΡΕΙΑ', '506901000', 'www.ampatzisepe.i-go.gr', '2014-03-17'),
(17, 'Α.΢.Κ. ΕΛΛΑ΢ ΕΣΑΙΡΕΙΑ ΠΕΡΙOΡΙ΢ΜΕΝΘ΢ ΕΤΘΤΝΘ΢ ΕΙ΢ΑΓΩΓΕ΢ - ΕΞΑΓΩΓΕ΢ - ΕΜΠΟΡΙΑ', '656701000', 'www.askhellas.gr/balancesheet', '2014-03-17'),
(18, 'ΜΠΟΤΣΛΑ΢ ΕΣΑΙΡΕΙΑ ΠΕΡΙΟΡΙ΢ΜΕΝΘ΢ ΕΤΘΤΝΘ΢', '696801000', 'www.boutlas.cpm', '2014-03-17'),
(19, 'Ν. ΓΕΩΡΓΟΠΟΥΛΟΣ ΙΔΙΩΤΙΚΗ ΚΕΦΑΛΑΙΟΥΧΙΚΗ ΕΤΑΙΡΕΙΑ', '000428301000', 'www.kat.ge.isoloonline.gr', '2016-04-20'),
(20, 'ΕΥΡΩΧΗΜΙΚΗ - Ι. ΜΑΡΑΤΟΣ - X. MAΡΑΤΟΥ ΙΚΕ', '57501000', NULL, '2016-05-06'),
(21, 'ΖΩΗ ΛΕΥΚΟΦΡΥΔΟΥ ΙΔΙΩΤΙΚΗ ΚΕΦΑΛΑΙΟΥΧΙΚΗ ΕΤΑΙΡΙΑ', '922301000', 'www.dimoprasiou.gr', '2017-03-31'),
(22, 'ΜΗΧΑΝΟΡΓΑΝΩΤΙΚΗ ΕΤΑΙΡΕΙΑ ΠΕΡΙΟΡΙΣΜΕΝΗΣ ΕΥΘΥΝΗΣ', '000991201000', 'www.focuswebtv.gr', '2015-10-27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `companies`
--
ALTER TABLE `companies`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `gemh_number` (`gemh_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `companies`
--
ALTER TABLE `companies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
