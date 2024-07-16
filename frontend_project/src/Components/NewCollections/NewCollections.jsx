import React from 'react'
import './NewCollections.css'
import gamepad2 from '../Assets/gamepad2.png'
import headset2 from '../Assets/headset2.png'
import Iphone from '../Assets/Iphone.png'
import keyboard from '../Assets/keyboard.png'
import laptop from '../Assets/laptop.png'
import Macbook from '../Assets/Macbook.png'
import smartphone from '../Assets/smartphone.png'
import sonywatch from '../Assets/sonywatch.png'
import soundspeaker from '../Assets/soundspeaker.png'
import Tab from '../Assets/Tab.png'
import tabaccessories from '../Assets/tabaccessories.png'
import camera2 from '../Assets/camera2.png'

const NewCollections = () => {
  return (
    <div className='newcollection'>
      <h1>Explore our Products</h1>
      <hr />
      <div className='collections'>
	<div className='collectionscontent'>
		<img src={gamepad2} alt="Gamepad" />
		<p>Gamepad</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={headset2} alt="Headset" />
		<p>Headset</p>
		<p>₦1000</p>

	</div>
	<div className='collectionscontent'>
		<img src={Iphone} alt="Iphone" />
		<p>Iphone</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={keyboard} alt="Keyboard" />
		<p>Keyboard</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={laptop} alt="Laptop" />
		<p>Laptop</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={Macbook} alt="Macbook" />
		<p>Macbook</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={smartphone} alt="Smart Phone" />
		<p>Smart Phone</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={sonywatch} alt="Sony Watch" />
		<p>Sony Watch</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={soundspeaker} alt="Sound Speaker" />
		<p>Sound Speaker</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={Tab} alt="Tab" />
		<p>Tab</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={tabaccessories} alt="Tab Accessories" />
		<p>Tab Accessories</p>
		<p>₦1000</p>
	</div>
	<div className='collectionscontent'>
		<img src={camera2} alt="Camera" />
		<p>Camera</p>
		<p>₦1000</p>
	</div>
      </div>
    </div>
  )
}

export default NewCollections
