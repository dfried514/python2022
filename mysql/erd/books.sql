-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema books_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema books_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `books_schema` DEFAULT CHARACTER SET utf8 ;
USE `books_schema` ;

-- -----------------------------------------------------
-- Table `books_schema`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_schema`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_schema`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_schema`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `books_schema`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `books_schema`.`favorites` (
  `authors_id` INT NOT NULL,
  `books_id` INT NOT NULL,
  INDEX `fk_favorites_authors_idx` (`authors_id` ASC) VISIBLE,
  INDEX `fk_favorites_books1_idx` (`books_id` ASC) VISIBLE,
  CONSTRAINT `fk_favorites_authors`
    FOREIGN KEY (`authors_id`)
    REFERENCES `books_schema`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_books1`
    FOREIGN KEY (`books_id`)
    REFERENCES `books_schema`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
