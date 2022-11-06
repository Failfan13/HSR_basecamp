export default function dataVisuals (data, title, order) {
    const dataContainer = document.querySelector('.info');
    const labels = ['mean', 'min', 'max', 'devi'];
    const dataBox = document.createElement('article');
    dataBox.style.order = order
    let dataId = document.createElement('p');
    dataId.className = 'dataId';
    dataId.innerHTML = title;
    dataBox.appendChild(dataId);
    for (let i = 0; i < 4; i++){
        let element = document.createElement('p');
        element.className = 'data';
        let codex = 0;
        if (labels[i] == labels[0]) {
            let sum = 0
            data[0].forEach(i => {
                sum += parseInt(i);
            })
            codex = sum / data[1][0]['points'].length
        }
        else if (labels[i] == labels[1]) {
            codex = Math.min.apply(Math, data[1][0]['points']).toFixed(2);
        }
        else if (labels[i] == labels[2]) {
            codex = Math.max.apply(Math, data[1][0]['points']).toFixed(2);
        }
        else if (labels[i] == labels[3]) {
            codex = math.std(data[1][0]['points'].map(Number)).toFixed(2)
        }
        element.innerHTML = labels[i]+': '+codex;
        dataBox.appendChild(element);
    }
    dataContainer.insertBefore(dataBox, dataContainer.childNodes[1]);
    document.createElement('p');
}