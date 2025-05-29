function  sum_char_codes(n: string): number {
  let sum = 0;
  for (let i =0); i < n.length ; ++i){
    sum += n.charCodeAt(i);
    
  }
return sum;
}
