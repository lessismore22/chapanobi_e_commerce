import React from 'react'
import './Popular.css'
import apple_product from '../Assets/apple_product.png'
import camera from '../Assets/camera.png'
import charger from '../Assets/charger.png'
import gamepad from '../Assets/gamepad.png'
import Headset from '../Assets/Headset.png'
import keyboard from '../Assets/keyboard.png'
import mouse from '../Assets/mouse.png'




const Popular = () => {
  return (
   <div className="popular">
    <h1>Today's Deals</h1>
    <hr />
    <div className="popular-images">
      <div className='image-container'>
      <img src={apple_product} alt="" />
      <p>Apple Charger</p>
      </div>
      <div className='image-container'>
      <img src={camera} alt="" />
      <p>Camera</p>
      </div>
      <div className='image-container'>
      <img src={charger} alt="" />
      <p>Charger</p>
      </div>
      <div className='image-container'>
      <img src={mouse} alt="" />
      <p>Mouse</p>
      </div>
      <div className='image-container'>
      <img src={gamepad} alt="" />
      <p>Gamepad</p>
      </div>
      <div className='image-container'>
      <img src={Headset} alt="" />
      <p>Headset</p>
      </div>
      <div className='image-container'>
      <img src={keyboard} alt="" />
      <p>Keyboard</p>
      </div>
    </div>
   </div>
  )
}

export default Popular;
