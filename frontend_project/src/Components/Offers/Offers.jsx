import React from 'react'
import './Offers.css'
import Appleheadset from '../Assets/Appleheadset.png'

const Offers = () => {
  return (
    <div className='offers'>
      <div className="offers-left">
	<h1>Enhance Your <br />Music Experience</h1>
	
	<button>Check Now</button>
      </div>
      <div className="offers-right">
	<img src={Appleheadset} alt="Apple headset" />
      </div>
    </div>
  )
}

export default Offers
