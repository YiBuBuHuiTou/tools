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

 Date: 30/12/2022 00:26:25
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
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES (1, 123, '2022-12-22', '09:00:00', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `record` VALUES (2, 5, '2022-12-27', '22:44:46', '22:50:19', NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (4, 5, '2022-12-28', '11:01:15', '20:37:45', NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (5, -495478576, '2022-12-28', '12:08:57', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (6, -464086832, '2022-12-28', '14:48:19', '16:24:09', NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (7, -536176432, '2022-12-28', '16:57:15', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (8, -245262128, '2022-12-28', '18:03:16', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (9, 5, '2022-12-29', '15:17:47', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (10, 6, '2022-12-29', '21:52:13', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (11, 7, '2022-12-29', '23:41:51', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (12, 8, '2022-12-29', '23:56:44', '23:58:07', NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (13, 8, '2022-12-30', '00:03:56', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (14, 10, '2022-12-30', '00:20:07', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (15, 11, '2022-12-30', '00:21:25', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (16, 135239888, '2022-12-30', '00:23:42', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (17, 12, '2022-12-30', '00:24:29', NULL, NULL, NULL, NULL, 0, NULL);
INSERT INTO `record` VALUES (18, 13, '2022-12-30', '00:25:31', NULL, NULL, NULL, NULL, 0, NULL);

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
-- Records of tenant
-- ----------------------------
INSERT INTO `tenant` VALUES (1, 'OBD', 5, 'asdf');
INSERT INTO `tenant` VALUES (2, 'CMU', 5, 'asdfasdf');
INSERT INTO `tenant` VALUES (3, 'OBD3434', 6, NULL);
INSERT INTO `tenant` VALUES (4, 'OBD343423', 6, NULL);
INSERT INTO `tenant` VALUES (5, 'APL', 7, NULL);

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
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (2, 'YiBuBuHuiTou', 123456, '591018214@qq.com', NULL, '09:00:00', '18:00:00', '测试用户');
INSERT INTO `user` VALUES (3, 'YiBuBuHuiTou4', 123456899, '591018214@qq.com2', NULL, '09:00:00', '17:00:00', '测试用户');
INSERT INTO `user` VALUES (4, 'YiBuBuHuiTou6', 123499568, '591018214@qq.com2', NULL, '09:00:00', '17:00:00', '');
INSERT INTO `user` VALUES (5, 'YiBuBuHuiTou2', 1234568, '591018214@qq.com2', NULL, '09:00:00', '17:00:00', '');
INSERT INTO `user` VALUES (6, 'YiBuBuHuiTou265', 123456854, '591018214@qq.com2', NULL, '08:00:00', '16:00:00', '345');
INSERT INTO `user` VALUES (7, 'YiBuBuHuiTou265123', 1234568542, '591018214@qq.co1m2', 'OBD343423', '07:00:00', '15:00:00', '345123123');
INSERT INTO `user` VALUES (8, 'shudiule', 106040, '591018214@qq.co1m2', 'OBD343423', '07:00:00', '15:00:00', '345123123');
INSERT INTO `user` VALUES (9, 'shudiule12', 106040, '591018214@qq.co1m2', 'OBD343423', '07:00:00', '15:00:00', '345123123');
INSERT INTO `user` VALUES (10, 'shudiule12345', 106040, '591018214@qq.co1m2', 'OBD343423', '07:00:00', '15:00:00', '345123123');
INSERT INTO `user` VALUES (11, 'shudiule12345678', 106040, '591018214@qq.co1m2', 'OBD343423', '07:00:00', '15:00:00', '345123123');
INSERT INTO `user` VALUES (12, 'shudiule12345678', 534, '591018214@qq.co1m2', 'OBD343423', '07:00:00', '15:00:00', '345123123');
INSERT INTO `user` VALUES (13, 'shudiule', 1060, '591018214@qq.co1m2', 'OBD', '07:00:00', '14:00:00', '345123123');

SET FOREIGN_KEY_CHECKS = 1;
