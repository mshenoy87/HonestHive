import React, {useEffect, useState} from 'react'
import {waggleAction} from './lookup'

export function ActionButton(props) {
  const {waggle, action, didPerformAction} = props;
  const likes = waggle.likes ? waggle.likes : 0;
  const className = props.className ? props.className : 'btn btn-primary btn-sm';
  const actionDisplay = action.type ? action.type : 'Action';

  const handleBackendEvent = (response, status) => {
    if ((status === 200 || status === 201) && didPerformAction) {
      didPerformAction(response, status);
    }
  }
  const handleClick = (event) => {
    event.preventDefault();
    waggleAction(waggle.id, action.type, handleBackendEvent);
  }
  const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay;
  return <button className={className} onClick={handleClick}>{display}</button>
}
