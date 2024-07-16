import React from 'react'
import './Hero.css'
import Headset from '../Assets/Headset.png'
import smart_watch from '../Assets/smart_watch.png'

const Hero = () => {
  return (
    <div className='hero'>
	<div className="hero-left">
		<h3>Roco Wireless <br /> Headphone </h3>
		<button className='hero-button'>Shop Now</button>
	</div>
	<div className="hero-right">
		<div className="hero-image">
			<img className='big-image' src={Headset} alt="" />
			<img className='small-image' src={smart_watch} alt="" />
			<div className='fast-sale'>Flash <br />Sales</div>
	</div>
	
	</div>
      
    </div>
  )
}

export default Hero;
