--
-- Tabellstruktur for tabell `user`
--

CREATE TABLE `user` (
  `id` smallint(12) NOT NULL,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL DEFAULT '''''''                                ''''''',
  `firstname` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `lastname` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(16) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dataark for tabell `user`
--

INSERT INTO `user` (`id`, `password`, `firstname`, `lastname`, `username`) VALUES
(1, '\'pbkdf2:sha256:150000$5LX2WMV4$0be1bd9dff6f414486d4fe6b08fe032b4e9f6677ba32407e996913cfe2107f61\'', 'Donald', 'Duck', 'donald');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;