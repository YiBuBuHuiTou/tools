/*
 Navicat Premium Data Transfer

 Source Server         : nacos
 Source Server Type    : MariaDB
 Source Server Version : 100607
 Source Host           : 127.0.0.1:3306
 Source Schema         : monitor

 Target Server Type    : MariaDB
 Target Server Version : 100607
 File Encoding         : 65001

 Date: 20/11/2022 20:04:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) NULL DEFAULT NULL,
  `start` time(0) NULL DEFAULT NULL,
  `end` time(0) NULL DEFAULT NULL,
  `overtime` float NULL DEFAULT NULL,
  `exchange_time` float NULL DEFAULT NULL,
  `reason` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `handled` tinyint(1) NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `job_num` int(11) NULL DEFAULT NULL COMMENT '工号',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `start` time(0) NULL DEFAULT NULL COMMENT '考勤-上班',
  `end` time(0) NULL DEFAULT NULL COMMENT '考勤-下班',
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
