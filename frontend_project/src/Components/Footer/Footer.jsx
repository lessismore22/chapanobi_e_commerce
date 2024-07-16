import React from 'react'
import './Footer.css'
import instagram_icon from '../Assets/instagram_icon.png'
import facebook_icon from '../Assets/facebook_icon.png'
import x_icon from '../Assets/x_icon.png'
import logo from '../Assets/logo.png'
import { Link } from 'react-router-dom'

const Footer = () => {
  return (
    <div className='footer'>
	<div className="footer-logo">
		<img src={logo} alt="Logo" />
		</div>
		<ul className='footer-links'>
			<Link to={"/"}>Home</Link>
			<Link to={"/About"}>About</Link>
			<Link to={"/Contact"}>Contact</Link>
		</ul>
		<div className="social-medial-icon">
			<div className="footer-icon-container">
				<img src={instagram_icon} alt="Intagram-Icon" />
			</div>
			<div className="footer-icon-container">
				<img src={facebook_icon} alt="Facebook-Icon" />
			</div>
			<div className="footer-icon-container">
				<img src={x_icon} alt="Twitter-Icon" />
			</div>
		</div>
		<div className="footer-copyrite">
			<hr />
			<p>copyrite @2024 - All rights Reserved</p>
		</div>
	
      
    </div>
  )
}

export default Footer;
