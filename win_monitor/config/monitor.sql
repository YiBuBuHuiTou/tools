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

 Date: 19/02/2023 21:01:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user` int(11) NOT NULL COMMENT '用户id',
  `date` date NOT NULL COMMENT '日期',
  `start` time(0) NULL DEFAULT NULL COMMENT '上班时间',
  `end` time(0) NULL DEFAULT NULL COMMENT '下班时间',
  `overtime` float NULL DEFAULT NULL COMMENT '加班时长',
  `exchange_time` float NULL DEFAULT NULL COMMENT '调休时长',
  `reason` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '加班理由',
  `handled` tinyint(1) NULL DEFAULT NULL COMMENT '是否已处理',
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `unique`(`user`, `date`) USING BTREE COMMENT '唯一约束'
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for tenant
-- ----------------------------
DROP TABLE IF EXISTS `tenant`;
CREATE TABLE `tenant`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '租户',
  `owner` int(11) NULL DEFAULT NULL COMMENT '拥有者',
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '描述',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `unique`(`name`) USING BTREE COMMENT '唯一约束'
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `job_num` int(11) NULL DEFAULT NULL COMMENT '工号',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `tenant` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '租户',
  `start` time(0) NULL DEFAULT NULL COMMENT '考勤-上班',
  `end` time(0) NULL DEFAULT NULL COMMENT '考勤-下班',
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- View structure for attendance_view
-- ----------------------------
DROP VIEW IF EXISTS `attendance_view`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `attendance_view` AS SELECT 
	USER.`name` AS '姓名',
	USER.`job_num` AS '工号',
	record.date AS '日期',
	( IFNULL( record.`start`, '昨天通宵' ) ) AS '上班时间',
	IFNULL( record.`end`, '今天通宵' ) AS '下班时间',
	IFNULL( record.`overtime`, 0 ) AS '计薪时间',
	IFNULL( record.`exchange_time`, 0 ) AS '调休时间',
	( CASE record.`handled` 
		WHEN 1 THEN
			'已处理' 
		ELSE 
			'未处理' 
		END ) AS '加班申请',
	IFNULL( record.`reason`, '' ) AS '加班理由' 
FROM `record`
		INNER JOIN `user` 
WHERE
	record.`user` = USER.`id` ;

SET FOREIGN_KEY_CHECKS = 1;
