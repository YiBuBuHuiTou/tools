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

 Date: 27/12/2022 19:22:03
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
  `date` datetime(0) NOT NULL COMMENT '日期',
  `start` time(0) NULL DEFAULT NULL COMMENT '上班时间',
  `end` time(0) NULL DEFAULT NULL COMMENT '下班时间',
  `overtime` float NULL DEFAULT NULL COMMENT '加班时长',
  `exchange_time` float NULL DEFAULT NULL COMMENT '调休时长',
  `reason` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '加班理由',
  `handled` tinyint(1) NULL DEFAULT NULL COMMENT '是否已处理',
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `unique`(`user`, `date`) USING BTREE COMMENT '唯一约束'
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of record
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL COMMENT '姓名',
  `job_num` int(11) NULL DEFAULT NULL COMMENT '工号',
  `email` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `start` time(0) NULL DEFAULT NULL COMMENT '考勤-上班',
  `end` time(0) NULL DEFAULT NULL COMMENT '考勤-下班',
  `description` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (2, 'YiBuBuHuiTou', 123456, '591018214@qq.com', '09:00:00', '18:00:00', '测试用户');
INSERT INTO `user` VALUES (3, 'YiBuBuHuiTou4', 123456899, '591018214@qq.com2', '09:00:00', '17:00:00', '测试用户');
INSERT INTO `user` VALUES (4, 'YiBuBuHuiTou6', 123499568, '591018214@qq.com2', '09:00:00', '17:00:00', '');
INSERT INTO `user` VALUES (5, 'YiBuBuHuiTou2', 1234568, '591018214@qq.com2', '09:00:00', '17:00:00', '');

SET FOREIGN_KEY_CHECKS = 1;
