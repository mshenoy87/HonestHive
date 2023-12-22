import React from "react";
import numeral from 'numeral';

export function FormatCount(props) {
    return <span className={props.className}>{numeral(props.children).format('0 a')}</span>;
}
