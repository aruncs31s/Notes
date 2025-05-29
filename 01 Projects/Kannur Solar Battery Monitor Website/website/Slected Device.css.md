```css
@import './base.css';

/* 
__
__
__

*/
.horizontal_layout{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    text-align: center;
    /* padding-bottom: 10rem; */
}

/* 
| | |
*/
.vert_layout{
    display: flex;
    flex-direction: row;
    justify-content: space-around;

}

.single-style{
    margin: 15px;
    padding: 20px;
    text-align: center;
    padding-bottom: 10rem;
    background-color: var(--nord1);
    border-radius: 5px;
    height: 50vh;
}
.card-layout{
    padding: 15px;
    margin: 0 auto;
    /* max-width: 1400px; */
    max-width: 95%;
    width: 100%;    
}
.card-chart-container{
    background-color: var(--nord1);
    border-radius: 10px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.25);
    transition: all 0.3s ease;
    margin: 0 10px 20px 10px;
    padding: 1rem;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    overflow: hidden;
    min-height: 300px;
}
.card-chart-container:hover {
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    transform: translateY(-5px);
}
    

.card-chart-container::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--nord8);
}

.chart-container{
    min-width: 75%;
    margin: 0 auto;

}
.chart-container-new {
    width: 100%;
    min-height: 350px;
    margin-top: 10px;
}

.device-control {
    display: flex;
    flex-direction: column;
    margin: auto;
}

.current-values {
    margin: 20px;
    padding: 20px;
    background-color: var(--nord1);
    border-radius: 5px;
}

.control-button {
    padding: 15px 30px;
    font-size: 18px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin: 10px;
    margin-bottom: 10px;
}

.control-button:hover {
    background-color: #45a049;
}

.control-button.active {
    background-color: #e74c3c;
}

.button-status {
    margin-top: 10px;
    font-style: italic;
}



/* main .device-status {
    margin: 20px;
    padding: 20px;
    background-color: var(--nord1);
    border-radius: 5px;
} */
/* 
main .row {
    display: flex;
    flex-direction: row;
    margin-left: 2rem;
    align-items: stretch;

} */
/* 
main .column-right {
    margin: auto;
    display: flex;
    flex-direction: column;
} */

/* .related-devices{
    background-color: var(--nord1);
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding-bottom: 100px;
    margin: 20px;
    border-radius: 10px;
    margin-bottom: 100px;
} */

/* .nearby-devices{
    background-color: var(--nord1);
    display: flex;
    flex-direction: column;
    justify-content: space-around;

} */
    /* flex-direction: column; */
    /* /* justify-content: space-around; */
    /* padding-bottom: 100px; */
    /* margin: 20px; */
    /* border-radius: 10px; */
    /* margin-bottom: 100px; */ 
/* .device-list{
    display: flex;
    /* flex-direction: column; */
    /* justify-content: space-around; */
    /* padding-bottom: 100px; */
    /* margin: 20px; */
    /* border-radius: 10px; */
    /* margin-bottom: 100px; */

 
/* #graph-container{
width: 33rem;
height: 20rem;
margin: 0 auto;

} */
/* .device-under-main-node{
    background-color: var(--nord1);
    display: flex;
    flex-direction: row;
    justify-content: space-around;
} */

/* Bouncing Box Styles */
.bouncing-box {
    width: 150px;
    height: 80px;
    background-color: var(--nord8);
    color: var(--nord0);
    border-radius: 8px;
    position: fixed;
    bottom: 30px;
    right: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(65, 119, 236, 0.3);
    z-index: 1000;
    animation: bounce 2s infinite;
    cursor: pointer;
    text-align: center;
    padding: 10px;
}

@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-15px);
    }
}

.bouncing-box:hover {
    animation-play-state: paused;
    background-color: var(--nord9);
}

/* Older Readings Section Styles */
.older_readings {
    margin-bottom: 2rem;
}

.older_readings h1 {
    margin: 1.5rem 0;
    text-align: center;
    color: var(--nord4);
}

/* Responsive layout for cards */
@media (max-width: 768px) {
    .vert_layout {
        flex-direction: column;
    }
    
    .card-chart-container {
        margin: 10px 0;
    }
}

.pad2m{
    padding: .2rem;
}

/*
New button style form 
https://getcssscan.com/css-buttons-examples

*/

/* CSS */
.button-30 {
  align-items: center;
  appearance: none;
  background-color: #FCFCFD;
  border-radius: 4px;
  border-width: 0;
  box-shadow: rgba(45, 35, 66, 0.4) 0 2px 4px,rgba(45, 35, 66, 0.3) 0 7px 13px -3px,#D6D6E7 0 -3px 0 inset;
  box-sizing: border-box;
  color: #36395A;
  cursor: pointer;
  display: inline-flex;
  font-family: "JetBrains Mono",monospace;
  height: 48px;
  justify-content: center;
  line-height: 1;
  list-style: none;
  overflow: hidden;
  padding-left: 16px;
  padding-right: 16px;
  position: relative;
  text-align: left;
  text-decoration: none;
  transition: box-shadow .15s,transform .15s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  will-change: box-shadow,transform;
  font-size: 18px;
}

.button-30:focus {
  box-shadow: #D6D6E7 0 0 0 1.5px inset, rgba(45, 35, 66, 0.4) 0 2px 4px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #D6D6E7 0 -3px 0 inset;
}

.button-30:hover {
  box-shadow: rgba(45, 35, 66, 0.4) 0 4px 8px, rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #D6D6E7 0 -3px 0 inset;
  transform: translateY(-2px);
}

.button-30:active {
  box-shadow: #D6D6E7 0 3px 7px inset;
  transform: translateY(2px);
}
```