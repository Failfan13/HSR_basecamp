import dataArrs from './modula/jsonRaspData.js';
import {createChart, createChartData} from './modula/chart.js';
import dataVisuals from './modula/interfaceData.js';

const screenWidth = (window.innerWidth > 0) ? window.innerWidth : screen.width;

const checkChar = () => {
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
        if (screenWidth < 1080 ){
            dataVisuals(data, title, order)
        }
        
        createChart(i.children, data[0], data[1])
        order++
    })
}

const uInteract = document.querySelectorAll('.btn')
const graphs = document.querySelectorAll('.chart')

const btnPress = (data) => {
    uInteract.forEach(i => {
        i.parentNode.removeAttribute('id')
    })
    if (screenWidth > 1080){
        graphs.forEach(i => {
            i.classList.remove(i.classList[3])
            i.className += ' seco'
            if (i.childNodes.length > 0){
                i.removeChild(i.childNodes[0])
            }
        })
        graphs.forEach(i => {
            if (i.classList[1] == data.path[0].classList[1]) {
                i.classList.remove('seco')
                i.className += ' main'
            }
        })
        checkChar()
    }
    else {
        graphs.forEach(i => {
            i.classList.remove(i.classList[2])
            i.className += ' hide'
            if (i.childNodes.length > 0){
                i.removeChild(i.childNodes[0])
            }
        })
        graphs.forEach(i => {
            if (i.classList[1] == data.path[0].classList[1]) {
                i.classList.remove('hide')
                i.className += ' show';
                const dataSet = document.querySelectorAll('#dataSet')
                dataSet.forEach(i => {
                    i.parentNode.removeChild(i)
                })
            }
        })
        checkChar()
    }
    data.path[1].id = 'select';
}
 
uInteract.forEach(i => {
    i.onclick = btnPress
})

checkChar()