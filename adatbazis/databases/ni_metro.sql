-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2023. Jan 28. 20:58
-- Kiszolgáló verziója: 10.4.27-MariaDB
-- PHP verzió: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `ni_metro`
--
CREATE DATABASE IF NOT EXISTS `ni_metro` DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;
USE `ni_metro`;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `dolgozo`
--

CREATE TABLE `dolgozo` (
  `id` int(11) NOT NULL COMMENT 'A dolgozó céges azonosítója',
  `nev` text NOT NULL COMMENT 'A dolgozó neve',
  `vezetoi` date DEFAULT NULL COMMENT 'Érvényes vezetői engedély lejárati dátuma (ha nincs, akkor NULL)',
  `segedvezetoi` date DEFAULT NULL COMMENT 'Érvényes segéd vezetői engedély lejárati dátuma (ha nincs, akkor NULL)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `dolgozo`
--

INSERT INTO `dolgozo` (`id`, `nev`, `vezetoi`, `segedvezetoi`) VALUES
(1, 'Gipsz Jakab', '2023-10-31', '2023-10-31'),
(2, 'Kiss János', NULL, '2023-10-31'),
(3, 'Nagy Géza', '2022-12-31', NULL),
(4, 'Fekete Árpád', '2024-01-01', '2023-02-07'),
(5, 'Ferencz Sándor', '2022-11-30', '2024-04-07'),
(6, 'Seres István', '2020-09-30', '2020-09-30'),
(7, 'Seresné Gizella', '2024-01-01', '2020-09-30'),
(8, 'Gondos József', '2024-02-27', '2024-02-27'),
(9, 'Kasza Blanka', NULL, NULL),
(10, 'Elek Géza', '2023-01-01', '2023-01-01'),
(11, 'Horváth Béla', '2024-02-27', '2024-02-27'),
(12, 'Kovács Attila', '2023-12-31', '2023-12-31'),
(13, 'Faragó Roland', '2023-12-31', '2023-12-31'),
(14, 'Szekeres Enikő', '2023-12-31', '2023-12-31'),
(15, 'Takács Gergő', '2024-02-17', NULL),
(16, 'Kis Elizabet', NULL, '2024-02-17'),
(17, 'Széles Ilona', '2024-12-31', '2024-12-31'),
(18, 'Péterfy Egon', '2022-01-01', NULL),
(19, 'Kovács István', '2024-12-31', '2024-12-31'),
(20, 'Szabó Zoltán', '2024-12-31', '2024-12-31');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `forda`
--

CREATE TABLE `forda` (
  `id` int(11) NOT NULL COMMENT 'A forda azonosítója',
  `kezdoido` time NOT NULL COMMENT 'Kezdés időpontja',
  `kezdoall` text NOT NULL COMMENT 'Kezdő állomás',
  `vegzoido` time NOT NULL COMMENT 'Végzés időpontja',
  `vegzoall` text NOT NULL COMMENT 'Végző állomás'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `forda`
--

INSERT INTO `forda` (`id`, `kezdoido`, `kezdoall`, `vegzoido`, `vegzoall`) VALUES
(1, '04:10:00', 'Örs Vezér tere', '13:16:00', 'Déli pályaudvar'),
(2, '04:20:00', 'Örs Vezér tere', '13:26:00', 'Déli pályaudvar'),
(3, '04:30:00', 'Örs Vezér tere', '13:36:00', 'Déli pályaudvar'),
(4, '04:31:00', 'Déli pályaudvar', '13:37:00', 'Örs Vezér tere'),
(5, '04:41:00', 'Déli pályaudvar', '13:47:00', 'Örs Vezér tere'),
(6, '13:16:00', 'Déli pályaudvar', '23:01:00', 'Kocsiszín'),
(7, '13:26:00', 'Déli pályaudvar', '23:11:00', 'Kocsiszín'),
(8, '13:36:00', 'Déli pályaudvar', '23:45:00', 'Déli pályaudvar'),
(9, '13:37:00', 'Örs Vezér tere', '23:30:00', 'Kocsiszín'),
(10, '13:47:00', 'Örs Vezér tere', '23:58:00', 'Déli pályaudvar');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `kocsi`
--

CREATE TABLE `kocsi` (
  `id` int(11) NOT NULL COMMENT 'A kocsi száma',
  `tipus` text NOT NULL COMMENT 'A kocsi tipusa',
  `szerelvenyid` int(11) NOT NULL COMMENT 'A szerelvény száma',
  `futottkm` int(11) NOT NULL COMMENT 'futott kilométer egészre kerekítve',
  `vizsga` date NOT NULL COMMENT 'a vizsga lejárati dátuma'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `kocsi`
--

INSERT INTO `kocsi` (`id`, `tipus`, `szerelvenyid`, `futottkm`, `vizsga`) VALUES
(110, 'Ev3', 1, 105725, '2024-03-31'),
(111, 'Ev3', 1, 105725, '2024-03-31'),
(112, 'EV3', 2, 221112, '2023-06-20'),
(113, 'Ev3', 2, 221112, '2023-06-20'),
(150, 'Ev3', 1, 105725, '2024-03-31'),
(151, 'Ev3', 1, 105725, '2024-03-31'),
(152, 'Ev3', 1, 105725, '2024-03-31'),
(153, 'Ev3', 1, 105725, '2024-03-31'),
(154, 'Ev3', 2, 221112, '2023-06-20'),
(155, 'Ev3', 2, 221112, '2023-06-20'),
(156, 'Ev3', 2, 221112, '2023-06-20'),
(157, 'Ev3', 2, 221112, '2023-06-20'),
(200, '81.717', 3, 450152, '2022-12-31'),
(201, '81.717', 3, 450152, '2022-12-31'),
(202, '81.717', 4, 15120, '2025-12-31'),
(203, '81.717', 4, 15120, '2025-12-31'),
(250, '81.714', 3, 450152, '2022-12-31'),
(251, '81.714', 3, 450152, '2022-12-31'),
(252, '81.714', 3, 450152, '2022-12-31'),
(253, '81.714', 3, 450152, '2022-12-31'),
(254, '81.714', 4, 15120, '2025-12-31'),
(255, '81.714', 4, 15120, '2025-12-31'),
(256, '81.714', 4, 15120, '2025-12-31'),
(257, '81.714', 4, 15120, '2025-12-31');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `menetrend`
--

CREATE TABLE `menetrend` (
  `sorszam` int(11) NOT NULL COMMENT 'Az adatbázis létrehozása óta közlekedett vonatok sorszáma',
  `datum` date NOT NULL COMMENT 'A menet közlekedési napja',
  `forda` int(11) NOT NULL COMMENT 'A forda azonosítója',
  `szerelvenyid` int(11) NOT NULL COMMENT 'A szerelvény azonosítója',
  `jarmuvezeto` int(11) NOT NULL COMMENT 'Jármű vezető',
  `segedvezeto` int(11) NOT NULL COMMENT 'Segéd vezető'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `menetrend`
--

INSERT INTO `menetrend` (`sorszam`, `datum`, `forda`, `szerelvenyid`, `jarmuvezeto`, `segedvezeto`) VALUES
(1, '2022-01-01', 1, 1, 15, 2),
(2, '2022-01-01', 2, 2, 18, 16),
(3, '2022-01-01', 3, 3, 1, 3),
(4, '2022-01-01', 4, 4, 4, 5),
(5, '2022-01-01', 5, 5, 6, 7),
(6, '2022-01-01', 6, 1, 8, 9),
(7, '2022-01-01', 7, 2, 10, 11),
(8, '2022-01-01', 8, 3, 12, 13),
(9, '2022-01-01', 9, 4, 14, 17),
(10, '2022-01-01', 10, 5, 19, 20);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `muhely`
--

CREATE TABLE `muhely` (
  `hibakod` int(11) NOT NULL COMMENT 'A hiba egyedi azonosítója',
  `szerelvenyid` int(11) NOT NULL COMMENT 'A szerelvény száma',
  `hiba` text NOT NULL COMMENT 'A hiba leírása',
  `kijavitva` tinyint(1) NOT NULL COMMENT 'A hiba kijavításának állapota (Igaz, ha ki lett javítva)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `muhely`
--

INSERT INTO `muhely` (`hibakod`, `szerelvenyid`, `hiba`, `kijavitva`) VALUES
(1, 1, 'Légsűritő néha nem működik', 1),
(2, 3, 'Légsűritő néha nem működik', 1),
(3, 2, 'Légsűritő néha nem működik', 1),
(4, 1, 'Fűtés nem működik', 0),
(5, 4, 'Légsűritő néha nem működik', 1),
(6, 5, 'Légsűritő néha nem működik', 1),
(7, 2, 'Főlégvezeték ereszt', 0),
(8, 2, 'Rögzítőfék lassan old', 0),
(9, 3, 'Légfék lassan old', 0),
(10, 1, 'Vonali rádió halk', 0);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `szerelveny`
--

CREATE TABLE `szerelveny` (
  `id` int(11) NOT NULL COMMENT 'A szerelvény száma',
  `becenev` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `szerelveny`
--

INSERT INTO `szerelveny` (`id`, `becenev`) VALUES
(1, 'Rendes'),
(2, 'Tamara'),
(3, 'Vizipók'),
(4, 'Elek'),
(5, 'Hisztis'),
(6, 'Szépség'),
(7, 'Főnök'),
(8, 'Heves'),
(9, 'Csiga'),
(10, 'Nő');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `dolgozo`
--
ALTER TABLE `dolgozo`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `forda`
--
ALTER TABLE `forda`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `kocsi`
--
ALTER TABLE `kocsi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `szerelvenyid` (`szerelvenyid`);

--
-- A tábla indexei `menetrend`
--
ALTER TABLE `menetrend`
  ADD PRIMARY KEY (`sorszam`),
  ADD KEY `datum` (`forda`),
  ADD KEY `szerelvenyid` (`szerelvenyid`,`jarmuvezeto`,`segedvezeto`),
  ADD KEY `datum_2` (`forda`);

--
-- A tábla indexei `muhely`
--
ALTER TABLE `muhely`
  ADD PRIMARY KEY (`hibakod`),
  ADD KEY `szerelvenyid` (`szerelvenyid`);

--
-- A tábla indexei `szerelveny`
--
ALTER TABLE `szerelveny`
  ADD KEY `id` (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `dolgozo`
--
ALTER TABLE `dolgozo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'A dolgozó céges azonosítója', AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT a táblához `forda`
--
ALTER TABLE `forda`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'A forda azonosítója', AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT a táblához `menetrend`
--
ALTER TABLE `menetrend`
  MODIFY `sorszam` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Az adatbázis létrehozása óta közlekedett vonatok sorszáma', AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT a táblához `muhely`
--
ALTER TABLE `muhely`
  MODIFY `hibakod` int(11) NOT NULL AUTO_INCREMENT COMMENT 'A hiba egyedi azonosítója', AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
