import dataArrs from './modula/jsonRaspData.js';
import {createChart, createChartData} from './modula/chart.js';
import dataVisuals from './modula/interfaceData.js';

const show = document.querySelectorAll('.show')

let order = 0
show.forEach(i => {
    let chart = document.createElement('canvas');
    let title = i.className.split(' ')[1]
    chart.id = title+' '+"myChart";
    i.appendChild(chart)
    if (title == 'every') {
        const allMeasure = ['temp', 'humid', 'press']
        const data = []
        const charData = []
        let count = 0
        allMeasure.forEach(i => {
            data.push(createChartData(dataArrs(), i))
            dataVisuals(data[0], i, order)
            charData.push(data[count][1][0])
            count++
        })
        createChart(i.children, data[0][0], charData)
        return
    } 
    let data = createChartData(dataArrs(), title)
    dataVisuals(data, title, order)
    createChart(i.children, data[0], data[1])
    order++
})

