echo "Eneter the number"
read n
fact=1
for((i=1;i<n;i++))
{
  fact=$((fact*i))
}
echo "factorial is $ fact"
