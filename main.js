const fs = require('fs');

const INPUT = './period.tsv';

function parseDate(date) {
    const [day, month, year] = date.split('/');
    return new Date(year, month - 1, day);
}

const rows = fs.readFileSync(INPUT, 'utf-8').split('\n').filter(el => el.trim().length > 0);
const tuples = rows.map(row => row.split('\t')).map(([base, rate, start, end, fee]) => ({base, rate, start, end, fee})).map((el, index) => {
    el.row = index + 2;
    el.rate = +el.rate.replace(',', '.');
    el.base = +el.base.replace(',', '.');
    el.start = new Date(parseDate(el.start));
    el.end = new Date(parseDate(el.end));
    el.fee = +el.fee.trim().replace(',', '.');
    return el;
});


// const selected = tuples.reduce((acc, el) => {
//     const key = el.start.toISOString().slice(0, 10);
//     if (!acc[key]) {
//         acc[key] = [];
//     }
//     acc[key].push(el);
//     return acc;
// }, {});
// for (const key in selected) {
//     if (selected[key].length <= 1) {
//         delete selected[key];
//     }
// }

fee = base * (rate / 100) * ((end - start) / 365);

const selected = tuples.reduce((acc, el) => {
    const key = el.fee;
    if (!acc[key]) {
        acc[key] = [];
    }
    acc[key].push(el);
    return acc;
}, {});
for (const key in selected) {
    if (key === '0' || selected[key].length <= 1) {
        delete selected[key];
    }
}


// const selected = tuples.filter(el => el.start.getDate() + 1 === el.end.getDate() && el.start.getMonth() === el.end.getMonth());


// const selected = tuples.filter(el => el.start.getDate() + 1 === el.end.getDate() && el.start.getMonth() === el.end.getMonth());

// const selected = tuples.filter(el => el.start.getMonth() === el.end.getMonth()).sort((x, y) => x.start.getMonth() - y.start.getMonth());

console.log(JSON.stringify(selected, null, 2));
