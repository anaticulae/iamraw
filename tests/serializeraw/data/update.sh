#! /usr/bin/bash

scriptpath=$(readlink -f "$0")
scriptroot=$(dirname "$scriptpath")

echo "update data"

pushd $scriptroot

todo="--border --text --fonts --horizontals --line -j4"
layout="--char_margin 5.0 --boxes_flow 1.0 --line_margin 0.3"

restructured=$(python -c 'import power; print(power.DOCU27_PDF)')
rawmaker -i ${restructured} -j8 --pages=0:21 ${todo} ${layout} -o restructured

groupme -i restructured -o restructured --footer --pagenumbers

rm "restructured/rawmaker__border_boundingboxes.yaml"
rm "restructured/rawmaker__line_line.yaml"
rm "restructured/rawmaker__horizontals_horizontals.yaml"
rm "restructured/groupme__pagenumbers_pagenumbers.yaml"

# TODO COMPARE $0 with SUCCESS
echo "done"

popd
