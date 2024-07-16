import React, { useContext } from 'react'
import { CartContext } from '../Context/CartContext';
import './Cart.css'

const Cart = () => {
  const { cartItems, updateQuantity, removeItem, total } = useContext(CartContext);
  const handleQuantityChange = (itemId, quantity) => {
    updateQuantity(itemId, quantity);
  };

  const handleRemoveItem = (itemId) => {
    removeItem(itemId);
  };
  return (
    <div className='cart-container'>
       <h1>Your Cart</h1>
      {cartItems.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <div>
          <ul className="cart-items">
            {cartItems.map((item) => (
              <li key={item.id} className="cart-item">
                <img src={item.image} alt={item.name} className="cart-item-image" />
                <div className="cart-item-details">
                  <h2>{item.name}</h2>
                  <p>${item.price}</p>
                  <div className="cart-item-controls">
                    <input
                      type="number"
                      min="1"
                      value={item.quantity}
                      onChange={(e) => handleQuantityChange(item.id, parseInt(e.target.value))}
                    />
                    <button onClick={() => handleRemoveItem(item.id)}>Remove</button>
                  </div>
                </div>
              </li>
            ))}
          </ul>
          <div className="cart-total">
            <h2>Total: ${total}</h2>
            <button>Proceed to Checkout</button>
          </div>
        </div>
      )}
      
    </div>
  );
};

export default Cart;
