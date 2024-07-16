import React, { useContext } from 'react'
import './Cartitems.css'
import { ShopContext } from '../../Context/Shopcontext'
import remove_icon from '../Assets/remove-icon.png'

const Cartitems = () => {
	const {all_product,cartitems,removeFromCart} = useContext(ShopContext);
  return (
    <div className='cartitems'>
	<div className='cartitems-format-main'>
		<p>Products</p>
		<p>Title</p>
		<p>Price</p>
		<p>Quatity</p>
		<p>Total</p>
		<p>Remove</p>
	</div>
	<hr />
	
	{all_product.map((e) => {
		if(cartitems[e.id]>0){
			return <div>
				<div className='cartitems-format'>
					<img src={e.image} alt="" className='carticon-product-icon' />
					<p>{e.name}</p>
					<p>${e.new_price}</p>
					<button className='cartitems-quantity'>{cartitems[e.id]}</button>
					<p>{e.new_price*cartitems[e.id]}</p>
					<img src={remove_icon} onClick={()=>{removeFromCart(e.id)}} alt='' />
				</div>
				<hr />
			</div>
		}})	
	}
      
</div>
  )
}

export default Cartitems
