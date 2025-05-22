const express = require('express');
const app = express();
const path = require('path');
const mysql = require('mysql2');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root_heslo123',
    database: 'ingrediences_recepies'
});

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.json());

app.get('/recipes', (req, res) => {
    const query = `
        select r.name as name, c.name as category, r.steps as steps, GROUP_CONCAT(i.name) as ingredients
        from Recipes r
        inner join categories c on r.category_id = c.id
        inner join RecipeIngredients ri on r.id = ri.recipe_id
        inner join ingrediences i on ri.ingredience_id = i.id
        group by r.id;
    `;
    connection.query(query, (err, rows) => {
        if (err) {
            console.error('Database error:', err);
            res.status(500).send
            return;
        }
        const processedRows = rows.map(row => ({
            ...row,
            ingredients: row.ingredients ? row.ingredients.split(',') : []
        }));

        return res.json(processedRows);
    });
});


app.get('/categories', (req, res) => {
    //res.json(categories);
    connection.query('SELECT * FROM categories', (err, rows) => {
        if (err) {
            res.status(500).send
            return;
        }
        return res.json(rows);
    });
});

app.get("/ingredients", (req, res) => {
//            res.json(ingredients);
    connection.query('SELECT * FROM ingrediences', (err, rows) => {
        if (err) {
            console.error('Chyba při dotazování databáze:', err);
            return res.status(500).send('Chyba při dotazování databáze');
        }
        return res.json(rows);
    });
});


const port = process.env.PORT || 80;
app.listen(port, () => {
    console.log('server is running');
});