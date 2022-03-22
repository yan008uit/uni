-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `attachment`
--

CREATE TABLE `attachment` (
  `id` int(11) NOT NULL,
  `size` varchar(10) CHARACTER SET latin1 NOT NULL DEFAULT '',
  `date` date NOT NULL DEFAULT current_timestamp(),
  `mimetype` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '',
  `filename` varchar(50) CHARACTER SET latin1 NOT NULL DEFAULT '',
  `code` mediumblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for table `attachment`
--
ALTER TABLE `attachment`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attachment`
--
ALTER TABLE `attachment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;