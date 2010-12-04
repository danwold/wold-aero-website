%rebase layout
Logbook Pro Extractor 0.2
<br>
<form action="/extractor" method="GET">

<table border="0" cellpadding="5">
<tr>
<th></th>
<th>time type</th>
<th>aircraft type</th>
<th>aircraft class</th>
<th>time duration</th>
<th>time increment</th>
</tr>

<tr>

<td>
<input type="submit" name="save3" value="submit">
</td>

<td>
<select name='typetime'>
<option name='duration' value='duration'>duration
<option name='instrument' value='instrument'>instrument
<option name='night' value='night'>night
<option name='instructor' value='instructor'>instructor
<option name='cc' value='cc'>cross country
<option name='pic' value='pic'>PIC
</select>
</td>

<td>
<select name='acbox'>
<option name='all' value='all'selected>all
%for ac in aclist:
<option name={{ac}} value={{ac}}> {{ac}}
%end
</select>
</td>

<td>
<select name='classbox'>
<option name='all' value='all'selected>all
<option name='AMEL' value='AMEL'>AMEL
<option name='ASEL' value='ASEL'>ASEL
<option name='ASES' value='ASES'>ASES
</select>
</td>

<td>
<input type='text' size='10' maxlength='10' name='timetext'>
</td>

<td>
<select name='timecombo'>
<option name='all' value='all'selected>all
<option name='days' value='days'>days
<option name='months' value='months'>months
<option name='years' value='years'>years
</select>
</td>

<td>
{{text}}
</td>
</tr>

</table>
{{acs}}

</font>
</form>

