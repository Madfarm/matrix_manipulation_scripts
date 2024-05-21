import './style.css'
import javascriptLogo from './javascript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.js'

document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="${viteLogo}" class="logo" alt="Vite logo" />
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
      <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
    </a>
    <h1>Hello Vite!</h1>
    <div class="card">
      <button id="counter" type="button"></button>
    </div>
    <p class="read-the-docs">
      Click on the Vite logo to learn more
    </p>
  </div>
`

setupCounter(document.querySelector('#counter'))

function gebi(e){return document.getElementById(e)}function drawCircle(e,r,a,i,n){n.beginPath(),n.arc(e,r,a,2*Math.PI,0),n.fillStyle=i,n.fill()}function drawRing(e,r,a,i,n){let l=1.6*a,t=.4*a;n.save(),n.beginPath(),n.ellipse(e,r,l,t,.2,i,2*Math.PI,!0),n.strokeStyle="brown",n.lineWidth=.4*a,n.stroke(),n.restore()}window.onload=function(){let e=gebi("canvas");e.style.background="black",document.body.style.margin=0;let r=e.getContext("2d");for(let e=0;e<planets.length;e++)planets[e].x=0;let a=window.performance.now();!function e(i){if(i-a>16.666666666666668){let e=canvas.width=window.innerWidth,a=canvas.height=window.innerHeight;r.clearRect(0,0,e,a);let i=e/800,l=e/2,t=a/2,d=[];d.push({x:l,y:t,size:60*i,color:"#FFCD00",draw:drawCircle});for(let e=0;e<planets.length;e++){let r=planets[e],a=r.size*i,o=r.orbit_radius*i,s=0,c=0;void 0!==r.skewx&&(s=r.skewx),void 0!==r.skewy&&(c=r.skewy);let w=l+Math.sin(r.angle)*o*(s+1),u={x:w,y:t+Math.cos(r.angle)*o*(c+.2),size:a,color:r.color,name:r.name,draw:r.draw};r.x<w?d.push(u):d.unshift(u),r.x=w,r.angle+=Math.PI/180/((n=r.speed)*(.03+1/(n+2)))*.007}for(let e=0;e<d.length;e++){let a=d[e];a.draw(a.x,a.y,a.size,a.color,r)}}var n;window.requestAnimationFrame(e)}(a)};const planets=[{name:"Mercury",color:"#dbfeff",size:2,speed:.2,orbit_radius:80,angle:0,draw:drawCircle},{name:"Venus",color:"#e84c09",size:6,speed:.6,orbit_radius:100,angle:.5,draw:drawCircle},{name:"Earth",color:"blue",size:6,speed:1,orbit_radius:130,angle:0,draw:function(e,r,a,i,n){drawCircle(e,r,a,i,n),drawCircle(e+a/3.5,r+a/3,a/3,"#06c400",n),drawCircle(e+a/3,r,a/3.4,"#06c400",n),drawCircle(e-a/3,r-a/3,a/3,"#06c400",n),drawCircle(e-a/2.5,r-a/2.5,a/2.5,"#06c400",n)}},{name:"Mars",color:"#e88b09",size:4,speed:1.9,orbit_radius:160,angle:0,draw:drawCircle},{name:"Jupiter",color:"#f94a04",size:23,speed:11.9,orbit_radius:220,angle:5,draw:drawCircle},{name:"Saturn",color:"#f7f7a8",size:15,speed:29.5,orbit_radius:280,angle:3,draw:function(e,r,a,i,n){drawRing(e,r,a,0,n),drawCircle(e,r,a,i,n),drawRing(e,r,a,Math.PI,n)}},{name:"Uranus",color:"#0acbfc",size:10,speed:84,orbit_radius:320,angle:1,draw:drawCircle},{name:"Neptune",color:"#7440dd",size:8,speed:164.8,orbit_radius:380,angle:2,draw:drawCircle}];