create database ingrediences_recepies
use ingrediences_recepies

create table ingrediences(
    id int primary key auto_increment,
    name varchar(255) not null
);

create table categories(
    id int primary key auto_increment,
    name varchar(255) not null
);

create table Recipes(
    id int primary key auto_increment,
    name varchar(255) not null,
    category_id int,
    steps varchar(10000) not null,
    portions float,
    foreign key (category_id) references categories(id)
);

create table RecipeIngredients(
    id int primary key auto_increment,
    recipe_id int,
    ingredience_id int,
    foreign key (recipe_id) references Recipes(id),
    foreign key (ingredience_id) references ingrediences(id)
);