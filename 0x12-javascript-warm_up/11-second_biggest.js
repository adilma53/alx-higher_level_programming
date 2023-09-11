#!/usr/bin/node




const args = process.argv.slice(2).map(Number);

if (args.length <= 1)
{
    console.log(0);
} else
{
    const largest = Math.max(...args);
    const removeLargest = [...args.filter(num => num !== largest];
    const secondLargest = Math.max(removeLargest);
    console.log(secondLargest);
}