import React, {useEffect, useState} from "react";
import { WaggleCreate } from "./create";
import {WaggleList} from './list';
import { FeedList } from "./feed";


export function WaggleComponent(props) {
  const [newWaggles, setNewWaggles] = useState([]);
  const canWaggle = props.canWaggle === "false" ? false : true;

  const handleNewWaggle = (newWaggles) =>{
    let tempNewWaggles = [...newWaggles];
    tempNewWaggles.unshift(newWaggles);
    setNewWaggles(tempNewWaggles);
  }

  return <div className={props.className}>
          {canWaggle === true && <WaggleCreate didTweet={handleNewWaggle} className='col-12 mb-3' />}
          <WaggleList newWaggles={newWaggles} {...props}/>
        </div>
}

export function FeedComponent(props) {
  const [newWaggles, setNewWaggles] = useState([]);
  const canWaggle = props.canWaggle === "false" ? false : true;

  const handleNewWaggle = (newWaggles) =>{
    let tempNewWaggles = [...newWaggles];
    tempNewWaggles.unshift(newWaggles);
    setNewWaggles(tempNewWaggles);
  }

  return <div className={props.className}>
          {canWaggle === true && <WaggleCreate didTweet={handleNewWaggle} className='col-12 mb-3' />}
          <FeedList newWaggles={newWaggles} {...props}/>
        </div>
}