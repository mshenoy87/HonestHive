import React, {useEffect, useState} from 'react';
import { apiWaggleFeed } from './lookup';
import { Waggle } from './detail';


export function FeedList(props) {
    const [wagglesInit, setWagglesInit] = useState([]);
    const [waggles, setWaggles] = useState([]);
    const [nextURL, setNextURL] = useState();
    const [wagglesDidSet, setWagglesDidSet] = useState(false);
  
    useEffect(() => {
      const final = [...props.newWaggles].concat(wagglesInit);
      if (final.length !== waggles.length) {
        setWaggles(final);
      }
    }, [props.newWaggles, waggles, wagglesInit]);
  
    useEffect(() => {
      if (wagglesDidSet === false) {
        const callback = (response, status) => {
          if (status === 200) {
            setNextURL(response.next);
            setWagglesInit(response.results);
            setWagglesDidSet(true);
          } 
        }
  
        apiWaggleFeed(callback, nextURL);
      }
    }, [wagglesInit, wagglesDidSet, setWagglesDidSet])
  
    const handleDidRewaggle = (newWaggle) => {
      const updateWagglesInit = [...wagglesInit];
      updateWagglesInit.unshift(newWaggle);
      setWagglesInit(updateWagglesInit);
      const updateFinalWaggles = [...waggles]
      updateFinalWaggles.unshift(waggles);
      setWaggles(updateFinalWaggles);
    }
    
    const handleLoadNext = (event) => {
      event.preventDefault();
      if (nextURL !== null) {
        const handleLoadNextResponse = (response, status) => {
          if (status === 200) {
            setNextURL(response.next);
            const newWaggles = [...waggles].concat(response.results);
            setWagglesInit(newWaggles);
            setWaggles(newWaggles);
          }
        }
        apiWaggleFeed(handleLoadNextResponse, nextURL);
      }
    }
  
    // return each waggle in the following format
    return <React.Fragment>
        {waggles.map((item, index)=>{
          return <Waggle
           waggle={item}
           key={`${index}-{item.id}`}
           didRewaggle={handleDidRewaggle}
           className='col-10 my-4 m-auto border px-2 py-3 bg-white text-dark'/>
        })}
        { nextURL !== null && <button onClick={handleLoadNext} className="btn btn-outline-primary">Load Next</button>}
    </React.Fragment>
  }
