import dataArrs from './modula/jsonRaspData.js';
import {createChart, createChartData} from './modula/chart.js';

const show = document.querySelectorAll('.show')

const dataVisuals = (data) => {
    const dataContainer = document.querySelector('.info');
    const labels = ['mean', 'min', 'max', 'devi']
    const dataBox = document.createElement('article')
    for (let i = 0; i <= 4; i++){
        let element = document.createElement('p')
        element.className = 'data';
        let codex = 0;
        if (labels[i] == labels[1]) {
            codex = Math.min.apply(Math, data[1][0]['points']).toFixed(2)
        }
        if (labels[i] == labels[2]) {
            codex = Math.max.apply(Math, data[1][0]['points']).toFixed(2)
        }
        element.innerHTML = labels[i]+': '+codex
        dataBox.appendChild(element)
    }
    dataContainer.insertBefore(dataBox, dataContainer.childNodes[0])
    document.createElement('p');
    console.log(data[1][0]['points'])
}

show.forEach(i => {
    let chart = document.createElement('canvas');
    let title = i.className.split(' ')[1]
    chart.id = title+' '+"myChart";
    i.appendChild(chart)
    let data = createChartData(dataArrs(), title)
    dataVisuals(data)
    createChart(i.children, data[0], data[1])
})