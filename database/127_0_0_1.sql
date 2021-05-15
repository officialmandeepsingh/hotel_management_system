-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 14, 2019 at 02:19 PM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotelmanagementdb`
--
CREATE DATABASE IF NOT EXISTS `hotelmanagementdb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `hotelmanagementdb`;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `catid` int(50) NOT NULL,
  `catname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`catid`, `catname`) VALUES
(11, 'Indian'),
(12, 'Breakfast'),
(14, 'drinks');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(20) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(200) NOT NULL,
  `phone_no` varchar(15) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `aadhar_no` varchar(20) NOT NULL,
  `reference` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `customer_name`, `dob`, `address`, `phone_no`, `email_id`, `aadhar_no`, `reference`) VALUES
(1, 'Mandeep Singh', '0000-00-00', 'Green Avenue\nBasti Peer Dad\nJalandhar	\n', '7837938605', 'mandeep@gmail.com', '1548/5698/7895', ''),
(2, 'a', '0000-00-00', 'Amritsar\n', '9874562154', 'abc@gmail.com', '154789654587', ''),
(3, 'abc', '1992-12-26', 'Amritsar\n', '9876543210', 'abc@gmail.com', '2547569884587', 'emp1');

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `srno` int(50) NOT NULL,
  `item_no` int(50) NOT NULL,
  `item_name` varchar(50) NOT NULL,
  `cat_name` varchar(50) NOT NULL,
  `Price` decimal(50,2) NOT NULL,
  `qty` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`srno`, `item_no`, `item_name`, `cat_name`, `Price`, `qty`) VALUES
(8, 0, 'Dosa', 'Indian', '80.00', 0);

-- --------------------------------------------------------

--
-- Table structure for table `res_bill`
--

CREATE TABLE `res_bill` (
  `srno` int(50) NOT NULL,
  `item_no` int(50) NOT NULL,
  `item_name` varchar(50) NOT NULL,
  `rate` decimal(15,2) NOT NULL,
  `qty` int(10) NOT NULL,
  `ammount` decimal(15,2) NOT NULL,
  `total_amt` decimal(15,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `srno` int(15) NOT NULL,
  `room_no` int(5) NOT NULL,
  `room_type` varchar(50) NOT NULL,
  `beds_rooms` int(5) NOT NULL,
  `people` int(10) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`srno`, `room_no`, `room_type`, `beds_rooms`, `people`, `status`) VALUES
(1, 1, 'Double', 1, 2, 'Book'),
(8, 5, 'Triple', 2, 3, 'Book');

-- --------------------------------------------------------

--
-- Table structure for table `room_history`
--

CREATE TABLE `room_history` (
  `room_no` int(20) NOT NULL,
  `room_type` varchar(50) NOT NULL,
  `customer_id` int(20) NOT NULL,
  `customer_name` varchar(20) NOT NULL,
  `check_in` date NOT NULL,
  `check_out` date NOT NULL,
  `advance_payment` double(20,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room_history`
--

INSERT INTO `room_history` (`room_no`, `room_type`, `customer_id`, `customer_name`, `check_in`, `check_out`, `advance_payment`) VALUES
(1, 'Double', 1, 'Mandeep Singh', '2019-07-14', '2019-07-15', 250.00),
(1, 'Double', 1, 'Mandeep Singh', '2019-07-17', '2019-07-25', 500.00),
(1, 'Double', 2, 'a', '2019-07-16', '2019-07-25', 500.00),
(5, 'Triple', 3, 'abc', '2019-07-14', '2019-07-14', 250.00);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `empid` int(50) NOT NULL,
  `ename` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `userid` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `doj` date NOT NULL,
  `usertype` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`empid`, `ename`, `dob`, `address`, `gender`, `phone`, `email`, `userid`, `password`, `doj`, `usertype`) VALUES
(5, 'Mandeep Singh', '1996-07-12', 'Jalandhar	\n', 'male', '7837938605', 'mandeep@gmail.com', 'mandeep', '1996', '2011-04-02', 'Admin'),
(6, 'Mandeep ', '1996-07-12', 'Jalandhar\n', 'male', '7837938605', 'mandeepemp@hotel.com', 'emp', '12', '2016-04-12', 'Employee'),
(7, 'hhj', '1996-07-12', 'ghj\n', 'male', '4454', '4534534', 'h', 'ghjg', '1998-07-15', 'Employee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`catid`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`srno`),
  ADD UNIQUE KEY `item_no` (`item_no`,`item_name`);

--
-- Indexes for table `res_bill`
--
ALTER TABLE `res_bill`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`srno`),
  ADD UNIQUE KEY `room_no` (`room_no`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`empid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `catid` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `srno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `res_bill`
--
ALTER TABLE `res_bill`
  MODIFY `srno` int(50) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `srno` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `empid` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
